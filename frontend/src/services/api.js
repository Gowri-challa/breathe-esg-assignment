import axios from "axios";

const API = axios.create({
  baseURL: "https://breathe-esg-assignment-jxdc.onrender.com/api",
});

export default API;