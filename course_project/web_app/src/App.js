import {
    Routes,
    Route,
} from "react-router-dom";
import MainPage from "./pages/MainPage";
import Profile from "./pages/Profile";
import Refferal from "./pages/Refferal";
import Vebinars from "./pages/Vebinars";
import FAQ from "./pages/FAQ";
import Rates from "./pages/Rates";


function App() {


    return (
        <Routes>
            <Route path="/" element={<MainPage/>}/>
            <Route path="/profile" element={<Profile/>}/>
            <Route path="/ref" element={<Refferal/>}/>
            <Route path="/veb" element={<Vebinars/>}/>
            <Route path="/rate" element={<Rates/>}/>
            <Route path="/faq" element={<FAQ/>}/>

        </Routes>
    );
}

export default App;
