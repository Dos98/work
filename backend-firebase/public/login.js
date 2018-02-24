(function(){
// Initialize Firebase
var config = {
    apiKey: "AIzaSyC19CtgLUhHbEjGDRj970eeHYeVyQ38_Bs",
    authDomain: "express-7190e.firebaseapp.com",
    databaseURL: "https://express-7190e.firebaseio.com",
    projectId: "express-7190e",
    storageBucket: "express-7190e.appspot.com",
    messagingSenderId: "1034098370699"
};
firebase.initializeApp(config);

const email = document.getElementById('em');
const pass = document.getElementById('pw');
const login  = document.getElementById('login');
const logout = document.getElementById('logout');
const signup = document.getElementById('signup');

login.addEventListener('click', e => {
    const ema = email.value;
    const passw = pass.value;
    console.log(ema);
    console.log(passw);
    const auth = fiebase.auth();
    const promise = auth.signInWithEmailAndPassword(ema, passw);
    promise.catch(e => console.log(e.message));
})

});