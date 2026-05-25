import { useState } from "react";
import API from "../services/api";

function UploadPage() {

  const [file, setFile] = useState(null);
  const [sourceType, setSourceType] = useState("SAP");

  const handleUpload = async () => {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("source_type", sourceType);

    try {

      const response = await API.post(
        "/upload/",
        formData
      );

      alert(response.data.message);

    } catch (error) {

      alert("Upload failed");
    }
  };

  return (

    <div className="page-container">

      <div className="card">

        <h1 className="title">
          Upload ESG Data
        </h1>

        <select
          className="select-box"
          value={sourceType}
          onChange={(e) =>
            setSourceType(e.target.value)
          }
        >

          <option value="SAP">SAP</option>

          <option value="UTILITY">
            Utility
          </option>

          <option value="TRAVEL">
            Travel
          </option>

        </select>

        <input
          className="file-input"
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
        />

        <button
          className="upload-btn"
          onClick={handleUpload}
        >
          Upload File
        </button>

      </div>

    </div>
  );
}

export default UploadPage;