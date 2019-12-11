//instalación

var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/styleBootstrap.css',
    '/static/core/img/doni.png'
];



self.addEventListener('install', function (event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

//Interceptación
self.addEventListener('fetch', function (event) {
    event.respondWith(
        fetch(event.request)
            .then(function (result) {
                return caches.open(CACHE_NAME)
                    .then(function (c) {
                        c.put(event.request.url, result.clone());
                        return result;
                    })
            })
            .catch(function (e) {
                return caches.match(event.request)
            })
    );
});



//Código Notificaciones Push
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyC_fx_PRteCj_4uWRR3iAgUVNSr3RsNGXo",
    authDomain: "frikiwaii.firebaseapp.com",
    databaseURL: "https://frikiwaii.firebaseio.com",
    projectId: "frikiwaii",
    storageBucket: "frikiwaii.appspot.com",
    messagingSenderId: "440249691222",
    appId: "1:440249691222:web:8a4ae8305dd95811fb1ff7"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {

    let title = payload.notification.title;

    let options = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }


    self.registration.showNotification(title, options);

});







