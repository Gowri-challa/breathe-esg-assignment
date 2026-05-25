import pandas as pd

from .serializers import EmissionRecordSerializer

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import Company, DataSource, EmissionRecord
from .utils import normalize_value


@api_view(['GET'])
def home(request):
    return Response({
        "message": "Breathe ESG Backend Running Successfully"
    })


@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):

    uploaded_file = request.FILES.get('file')

    source_type = request.data.get('source_type')

    if not uploaded_file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    df = pd.read_csv(uploaded_file)

    company, _ = Company.objects.get_or_create(
        name="Demo Company"
    )

    datasource = DataSource.objects.create(
        company=company,
        source_type=source_type
    )

    records_created = 0

    for _, row in df.iterrows():

        suspicious = False

        if source_type == "SAP":

            value = row['quantity']
            unit = row['unit']

            normalized = normalize_value(value, unit)

            if value < 0:
                suspicious = True

            EmissionRecord.objects.create(
                source=datasource,
                category="Scope 1",
                activity_type=row['fuel_type'],
                original_value=value,
                original_unit=unit,
                normalized_value=normalized,
                normalized_unit="kgCO2e",
                co2e=normalized,
                suspicious_flag=suspicious
            )

        elif source_type == "UTILITY":

            value = row['kwh']

            normalized = normalize_value(value, "kwh")

            if value > 10000:
                suspicious = True

            EmissionRecord.objects.create(
                source=datasource,
                category="Scope 2",
                activity_type="Electricity",
                original_value=value,
                original_unit="kwh",
                normalized_value=normalized,
                normalized_unit="kgCO2e",
                co2e=normalized,
                suspicious_flag=suspicious
            )

        elif source_type == "TRAVEL":

            value = row['distance_km']

            normalized = normalize_value(value, "km")

            if value > 8000:
                suspicious = True

            EmissionRecord.objects.create(
                source=datasource,
                category="Scope 3",
                activity_type="Business Travel",
                original_value=value,
                original_unit="km",
                normalized_value=normalized,
                normalized_unit="kgCO2e",
                co2e=normalized,
                suspicious_flag=suspicious
            )

        records_created += 1

    return Response({
        "message": "File uploaded successfully",
        "records_created": records_created
    })


# GET ALL RECORDS API
@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all()

    serializer = EmissionRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


# APPROVE RECORD API
@api_view(['POST'])
def approve_record(request, id):

    record = EmissionRecord.objects.get(id=id)

    record.status = "APPROVED"

    record.save()

    return Response({
        "message": "Record approved"
    })


# REJECT RECORD API
@api_view(['POST'])
def reject_record(request, id):

    record = EmissionRecord.objects.get(id=id)

    record.status = "REJECTED"

    record.save()

    return Response({
        "message": "Record rejected"
    })