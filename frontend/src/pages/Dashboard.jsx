import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {

  const [records, setRecords] = useState([]);

  useEffect(() => {

    fetchRecords();

  }, []);

  const fetchRecords = async () => {

    const response = await API.get(
      "/records/"
    );

    setRecords(response.data);
  };

  const approvedCount = records.filter(
    (r) => r.status === "APPROVED"
  ).length;

  const rejectedCount = records.filter(
    (r) => r.status === "REJECTED"
  ).length;

  const suspiciousCount = records.filter(
    (r) => r.suspicious_flag
  ).length;

  return (

    <div className="page-container">

      <div className="card">

        <h1 className="title">
          ESG Dashboard
        </h1>

        <div className="dashboard-grid">

          <div className="dashboard-card">
            <h2>{records.length}</h2>
            <p>Total Records</p>
          </div>

          <div className="dashboard-card">
            <h2>{approvedCount}</h2>
            <p>Approved</p>
          </div>

          <div className="dashboard-card">
            <h2>{rejectedCount}</h2>
            <p>Rejected</p>
          </div>

          <div className="dashboard-card">
            <h2>{suspiciousCount}</h2>
            <p>Suspicious</p>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;