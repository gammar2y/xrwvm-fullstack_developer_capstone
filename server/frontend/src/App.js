import LoginPanel from "./components/Login/Login"
import Register_panel from "./components/Register/Register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register_panel />}> </Route>
    </Routes>
  );
}
export default App;
