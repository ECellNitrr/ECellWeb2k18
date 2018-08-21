var sponsors_html = document.querySelector('.patreons');
var this_container = document.querySelector('#this_spons')
var prev_container = document.querySelector('#prev_spons')
var this_spons_div = document.querySelector('#this_spons div')
var prev_spons_div = document.querySelector('#prev_spons div')

var type = {
    'AS': 'Associate Sponsors',
    'PLTS': 'Platinum Sponsors',
    'GS': 'Gold Sponsors',
    'TS': 'Title Sponsors',
    'PRTS': 'Partner Sponsors',
}

fetch(base_url + '/sponsors/list/')
    .then(data => data.json())
    .then(function (data) {
        document.querySelector('#spinner').remove();
        var sponsors = data.spons;
        var this_spons = []
        var prev_spons = []

        sponsors.forEach(type => {
            type.sponsors.forEach(function (sponsor) {
                if (sponsor.year == 2018) {
                    this_spons.push(sponsor)
                    this_container.style.display = 'block'
                } else {
                    prev_spons.push(sponsor)
                    prev_container.style.display = 'block'
                }
            })
        })

        insert_sponsors(this_spons,this_spons_div)
        insert_sponsors(prev_spons,prev_spons_div)

        console.log(JSON.stringify(this_spons, null, 2))
        console.log(JSON.stringify(prev_spons, null, 2))
    })

insert_sponsors = (spons, location) => {
    spons.forEach(function (sponsor) {
        location.innerHTML += ` 
                <div class='sponsor'>
                    <img src='${sponsor.pic}'>
                    <div class='details'>
                        <h2>${sponsor.name}</h2>
                        <p class='body'>${sponsor.details}</p>
                        <p class='contact_no'>${sponsor.contact}</p>
                        <p class='website'><a href='${sponsor.website}'>website</a></p>
                    </div>
                </div>`;
    })
}