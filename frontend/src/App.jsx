import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import UploadPage from "./pages/UploadPage";
import Dashboard from "./pages/Dashboard";
import ReviewPage from "./pages/ReviewPage";

function App() {

  return (

    <BrowserRouter>

      <div>

        <nav className="navbar">

          <Link to="/">
            Upload
          </Link>

          <Link to="/dashboard">
            Dashboard
          </Link>

          <Link to="/review">
            Review
          </Link>

        </nav>

        <Routes>

          <Route
            path="/"
            element={<UploadPage />}
          />

          <Route
            path="/dashboard"
            element={<Dashboard />}
          />

          <Route
            path="/review"
            element={<ReviewPage />}
          />

        </Routes>

      </div>

    </BrowserRouter>
  );
}

export default App;