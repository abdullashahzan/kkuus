importScripts('https://www.gstatic.com/firebasejs/10.9.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.9.0/firebase-messaging-compat.js');

const firebaseConfig = {
    apiKey: "AIzaSyBSCpcctpJNIr26-D73N9-M6Jhxe3pZnk0",
    authDomain: "kku-unofficial-store.firebaseapp.com",
    projectId: "kku-unofficial-store",
    storageBucket: "kku-unofficial-store.appspot.com",
    messagingSenderId: "920854395385",
    appId: "1:920854395385:web:2c52cbe92d41289d912528"
};

firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

let appeared = 0;

messaging.onBackgroundMessage((payload) => {
    if (appeared == 0) {
        const notificationTitle = payload.notification.title;
        const notificationOptions = {
            body: payload.notification.body,
        };
        self.registration.showNotification(notificationTitle, notificationOptions);
        appeared += 1
    }
});