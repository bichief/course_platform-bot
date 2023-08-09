import {useEffect, useState} from "react";
import axios from "axios";
import {API_URL} from "../constants";

const [user, setUser] = useState(null);
useEffect(() => {
    axios.get(API_URL).then((response) => {
        setUser(response.data);
    });
}, []);
console.log(user)