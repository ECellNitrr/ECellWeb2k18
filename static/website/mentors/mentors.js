var this_mentors = document.querySelector('#this_year .people')
var prev_mentors = document.querySelector('#prev_year .people')
var this_div = document.querySelector('#this_year')
var prev_div = document.querySelector('#prev_year')

fetch(base_url + '/mentors/list/')
    .then(data => data.json())
    .then(function (data) {
        document.querySelector('#spinner').remove();
        var mentors = data.mentors
        var this_data = mentors.filter(ele => ele.year == 2018)
        var prev_data = mentors.filter(ele => ele.year != 2018)

        insert_mentors(this_data, this_mentors)
        insert_mentors(prev_data, prev_mentors)

        if (this_data.length) this_div.style.display = 'block'
        if (prev_data.length) prev_div.style.display = 'block'

        // console.log(JSON.stringify(this_data, null, 2))
        // console.log(JSON.stringify(prev_data, null, 2))


    })


insert_mentors = (mentors, location) => {
    mentors.forEach(function (mentor) {
        // console.log(mentor);
        location.innerHTML += (`
            <div>
                <img class="" src='${mentor.profile_pic}' alt="">
                    <div class="">
                    <h3>${mentor.name}</h3>
                    <h4>${mentor.detail}</h4>
                </div>
            </div>
        `)
    })
}