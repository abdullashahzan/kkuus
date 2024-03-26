function openModalParameter(item_id) {
    document.getElementById('myModal').style.display = 'block';
    var item_id = item_id.trim();
    console.log(item_id);
    document.querySelector('.redirect_link').action = `/myShop/renew/${item_id}`;
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function openModal() {
    document.getElementById('myModal').style.display = 'block';
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
}

let lastScrollTop = 0;
const hiddenDiv = document.getElementById("hiddenDiv");

window.addEventListener("scroll", function () {
    let currentScroll = window.scrollY;
    if (currentScroll > lastScrollTop) {
        // Scroll down
        hiddenDiv.classList.remove("animate__slideInUp");
        hiddenDiv.classList.add("animate__slideOutDown");
        hiddenDiv.addEventListener("animationend", function () {
            hiddenDiv.classList.remove("d-none");
            hiddenDiv.classList.add("d-block");
        });
    } else {
        // Scroll up
        hiddenDiv.classList.remove("animate__slideOutDown");
        hiddenDiv.classList.add("animate__slideInUp");
    }
    lastScrollTop = currentScroll;
});

document.addEventListener("DOMContentLoaded", function () {
    var forms = document.querySelectorAll("form");

    forms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            var submitButton = form.querySelector("button[type='submit']");
            submitButton.disabled = true;

            // Optional: Display a loading indicator
            submitButton.innerHTML = "Please wait...";

            // Prevent the default form submission behavior
            event.preventDefault();

            // Manually submit the form after a short delay (optional)
            setTimeout(function () {
                form.submit();
            }, 200); // Adjust the delay as needed
        });
    });
});


var csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
function saveTokenToServer(token) {
    // Make an AJAX request to your server to save the token
    fetch('/save-fcm-token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ token: token }),
    }).then(response => {
        if (response.ok) {
            console.log('Token saved successfully on the server');
        } else {
            console.error('Failed to save token on the server');
        }
    }).catch(error => {
        console.error('Error saving token on the server:', error);
    });
}
// Initialize Firebase
const firebaseConfig = {
    apiKey: "AIzaSyBSCpcctpJNIr26-D73N9-M6Jhxe3pZnk0",
    authDomain: "kku-unofficial-store.firebaseapp.com",
    projectId: "kku-unofficial-store",
    storageBucket: "kku-unofficial-store.appspot.com",
    messagingSenderId: "920854395385",
    appId: "1:920854395385:web:2c52cbe92d41289d912528"
};
firebase.initializeApp(firebaseConfig);

// Initialize Firebase Messaging
const messaging = firebase.messaging();

// Request permission for push notifications and get token
messaging.getToken({ vapidKey: 'BI6I-N5Wyy7XV5XLnHSa6DmvxPqJaHgb0kU2ir4--MA_4w69A4y1o7108p-5g7DPny7edALN_z_DkkziBKa1nK0' }) // Replace 'YOUR_VAPID_KEY' with your actual VAPID key
    .then((currentToken) => {
        if (currentToken) {
            console.log('Token:', currentToken);
            // Send this token to your server to associate with the user
            saveTokenToServer(currentToken);
        } else {
            console.log('No registration token available. Request permission to generate one.');
            // Show permission request UI
        }
    })
    .catch((error) => {
        console.log('Error getting token:', error);
    });

// Check if the browser supports service workers
if ('serviceWorker' in navigator) {
    // Register service worker
    navigator.serviceWorker.register('/firebase-messaging-sw.js')
    .then(function(registration) {
        console.log('Service Worker registered with scope:', registration.scope);
        
        // Subscribe to push notifications
        registration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: 'BI6I-N5Wyy7XV5XLnHSa6DmvxPqJaHgb0kU2ir4--MA_4w69A4y1o7108p-5g7DPny7edALN_z_DkkziBKa1nK0' // Replace 'YOUR_PUBLIC_KEY' with your actual VAPID key
        })
        .then(function(subscription) {
            console.log('Push notification subscription:', subscription);
            // Send subscription information to your server for future use
            saveTokenToServer(subscription); // Call saveTokenToServer function with the subscription object
        })
        .catch(function(error) {
            console.error('Push subscription error:', error);
        });
    })
    .catch(function(error) {
        console.error('Service Worker registration failed:', error);
    });
}

// Handle incoming messages when app is in foreground
messaging.onMessage((payload) => {
    console.log('Message received:', payload);
    // Handle notification here, e.g., display a notification to the user
});

// Handle background messages by registering a service worker
navigator.serviceWorker.register('/firebase-messaging-sw.js')
    .then((registration) => {
        console.log('Service worker registered:', registration);
    })
    .catch((error) => {
        console.error('Service worker registration failed:', error);
    });
