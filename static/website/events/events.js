$(function () {
    var events = $('#articles')
    $.get('http://ecellnitrr.herokuapp.com/event/list/').then(function (data) {
        data.Events.forEach(function (event, i) {
            if (i % 2 == 0) {
                events.append(`
                <article>
                    <div class=article-layout>
                        <div class=text>
                            <h2 class="wow fadeInLeft">${event.name}</h2>
                            <p class="wow fadeInUp">${event.details}</p>
                        </div>
                        <div class="img wow fadeInRight">
                            <img src='http://ecellnitrr.herokuapp.com/${event.cover_pic}' alt=""> </div>
                    </div>
                </article>
                `)
            } else {
                events.append(`
                <div class=right-grey>
                    <svg xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                        <polygon points="100 0 100 10 0 10" /> </svg>
                </div>
                <article class=reverse-layout>
                    <div class=article-layout>
                        <div class=text>
                            <h2 class="wow fadeInRight">${event.name}</h2>
                            <p class="wow fadeInUp">${event.details}</p>
                        </div>
                        <div class="img wow fadeInLeft">
                            <img src='http://ecellnitrr.herokuapp.com/${event.cover_pic}' alt=""> </div>
                    </div>
                </article>
                <div class=right-white>
                    <svg xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                        <polygon points="100 0 100 10 0 10" /> </svg>
                </div>
                `)
            }
        })
    })
})