// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDVK6zJp9n-AYty-N9R5RGwK7SFTvnvE7g",
  authDomain: "sadfi-pbl-011.firebaseapp.com",
  projectId: "sadfi-pbl-011",
  storageBucket: "sadfi-pbl-011.appspot.com",
  messagingSenderId: "575818532473",
  appId: "1:575818532473:web:c5229b8d6c0aea663d76a8",
  measurementId: "G-RPNNW8V5CJ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);