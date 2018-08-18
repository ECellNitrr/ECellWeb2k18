var events = document.querySelector('#articles')

put_events_in_place = (data) => {
    
    
    events.innerHTML += (`
            <article>
                <div class=article-layout>
                    <div class=text>
                        <h2 class=""><a href="/event_detail/${event.id}">${event.name}</a></h2>
                        <p><strong>Venue: </strong>${event.venue} on ${event.date} at ${event.time}</p>
                        <p>${event.details}</p>
                        <div class='center_btn'>
                            <button class="register_btn" data-eid=${event.id}>Register</button>
                        </div>
                    </div>
                    <div class="img ">
                        <img src='${event.cover_pic}' alt=""> </div>
                </div>
            </article>
        `)
}

$(function () {
    $.get('/event/list/').then(function (data) {
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
