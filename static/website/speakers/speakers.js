var this_year_loc = document.querySelector('#this_year')
var prev_year_loc = document.querySelector('#prev_year')
var this_div = document.querySelector('#this_div')
var prev_div = document.querySelector('#prev_div')
var heading = document.querySelectorAll('.heading')

// console.log(this_year_loc, prev_year_loc)

fetch(base_url + '/speakers/list/')
    .then(data => data.json())
    .then(function (data) {
        document.querySelector('#spinner').remove()
        if(data.success == true){
            var speakers = data.speakers
            var this_year = speakers.filter(e => e.year == 2018)
            var prev_years = speakers.filter(e => e.year != 2018)

            if (this_year.length) this_div.style.display = 'block'
            if (prev_years.length) prev_div.style.display = 'block'

            insert_speakers(this_year, this_year_loc)
            insert_speakers(prev_years, prev_year_loc)

            // display the speakers
            heading.forEach(ele => ele.style.display = 'block')
        }else{
            this_div.style.display = 'block'
            this_div.innerHTML += `<center><h3>Coming Soon</h3></center>`
        }
    })

function insert_speakers(speakers, location) {
    speakers.forEach(speaker => {
        location.innerHTML +=
            `<div class='speaker row'>
                <div class='s-img text-center align-items-center col-lg-4'>
                    <img src='${speaker.profile_pic}'>
                </div>
                <div class='s-info justify-content-center align-items-center col-lg-7'>
                    <div>
                        <h4 class='name'>${speaker.name}</h4>
                        <h5 class='company'>( ${speaker.company} )</h5>
                        <div class='year'><span>Year: </span>${speaker.year}</div>
                        <p class='desc text-justify mt-3'>${speaker.description !== 'none' ? speaker.description : ''}</p>
                        <div>
                            <a href='${speaker.social_media}' class='social_media'><i class='fa fa-anchor'></i> Follow on social media </a>
                        </div>
                    </div>
                </div>
            </div>`
    })
}