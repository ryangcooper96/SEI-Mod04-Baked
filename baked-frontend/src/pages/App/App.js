import { Route, Routes } from "react-router-dom";
import { useEffect, useState } from "react";

import NavBar from "../../components/NavBar/NavBar";

import collection from "../../utils/company";
import "./App.css";

import HomePage from "../HomePage/HomePage";
import LoginPage from "../LoginPage/LoginPage";

function App() {
  // state
  const [result, setResult] = useState({});

  // useEffect
  useEffect(() => {
    async function getResult() {
      const data = await collection.get();
      setResult({ ...data });
      console.log(data);
    }
    getResult();
  }, []);

  return (
    <div className="App">
      <NavBar />
      <Routes>
        <Route exact path="/" element={<HomePage />} />
        <Route exact path="/login" element={<LoginPage />} />
      </Routes>
    </div>
  );
}

export default App;
