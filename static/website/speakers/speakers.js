var this_year_loc = document.querySelector('#this_year')
var prev_year_loc = document.querySelector('#prev_year')
var heading = document.querySelectorAll('.heading')

console.log(this_year_loc, prev_year_loc)

fetch(base_url + '/speakers/list/')
    .then(data => data.json())
    .then(function (data) {
        document.querySelector('#spinner').remove()
        heading.forEach(ele => ele.style.display = 'block')

        var speakers = data.speakers
        var this_year = speakers.filter(e => e.year == 2018)
        var prev_years = speakers.filter(e => e.year != 2018)

        console.log(JSON.stringify(this_year, null, 2))
        console.log(JSON.stringify(prev_years, null, 2))

        insert_speakers(this_year, this_year_loc)
        insert_speakers(prev_years,prev_year_loc)

    })

function insert_speakers(speakers, location) {
    speakers.forEach(speaker => {
        location.innerHTML +=
            `<div>
                <div class='s-img text-center'>
                    <img src='${speaker.profile_pic}'>
                </div>
                <div class='s-info'>
                    <div>
                        <h4>${speaker.name}</h4>
                        <h5 class='company'>${speaker.company}</h5>
                        <div class='year'>${speaker.year}</div>
                        <p class='desc'>${speaker.description}</p>
                        <div class='text-right'>
                            <a href='${speaker.social_media}' class='social_media'><i class='fa fa-anchor'></i><strong> follow</strong></a>
                        </div>
                    </div>
                </div>
            </div>`
    })
}