<<<<<<< HEAD
var events = document.querySelector('#articles')
=======
$(function () {
    var events = $('#articles')
    $.get(base_url + '/event/list/').then(function (data) {
        $('#spinner').hide(1000);
>>>>>>> 97f3f6cd0bbdc4071f931eea68fdfc85de641dc8

put_events_in_place = (data) => {
    data.Events.forEach(function (event, i) {
        if (i % 2 == 0) {
            events.innerHTML += (`
            <article>
                <div class=article-layout>
                    <div class=text>
                        <h2 class="">${event.name}</h2>
                        <p><strong>Venue: </strong>${event.venue} on ${event.date} at ${event.time}</p>
                        <p>${event.details}</p>
                        <div class='center_btn'>
                            <button class="register_btn" data-eid=${event.id}>Register</button>
                        </div>
<<<<<<< HEAD
=======
                        <div class="img ">
                            <img src='/${event.cover_pic}' alt=""> </div>
>>>>>>> 97f3f6cd0bbdc4071f931eea68fdfc85de641dc8
                    </div>
                    <div class="img ">
                        <img src='${event.cover_pic}' alt=""> </div>
                </div>
            </article>
            `)
        } else {
            events.innerHTML +=(`
            <div class=right-grey>
                <svg xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                    <polygon points="100 0 100 10 0 10" /> </svg>
            </div>
            <article class=reverse-layout>
                <div class=article-layout>
                    <div class=text>
                        <h2 class="">${event.name}</h2>
                        <p><strong>Venue: </strong>${event.venue} on ${event.date} at ${event.time}</p>
                        <p>${event.details}</p>
                        <div class='center_btn'>
                            <button class="register_btn" data-eid=${event.id}>Register</button>
                        </div>
<<<<<<< HEAD
=======
                        <div class="img ">
                            <img src='/${event.cover_pic}' alt=""> </div>
>>>>>>> 97f3f6cd0bbdc4071f931eea68fdfc85de641dc8
                    </div>
                    <div class="img ">
                        <img src='${event.cover_pic}' alt=""> </div>
                </div>
            </article>
            <div class=right-white>
                <svg xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                    <polygon points="100 0 100 10 0 10" /> </svg>
            </div>
            `)
        }
    })
}

$(function () {
    $.get('list/').then(function (data) {
        console.log(data)
        // hide the spinner
        $('#spinner').hide(1000);
        // put data
        put_events_in_place(data)
        // to add event listener
        register_stuff(data)
    })
})

// document.querySelector('#spinner').remove();
// put_events_in_place(data)
// register_stuff(data)
