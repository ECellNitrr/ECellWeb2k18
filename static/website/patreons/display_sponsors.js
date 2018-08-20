let sponsors_html = document.querySelector('.patreons');
let sponsors = null;

let type = {
    'AS': 'Associate Sponsors',
    'PLTS': 'Platinum Sponsors',
    'GS': 'Gold Sponsors',
    'TS': 'Title Sponsors',
    'PRTS': 'Partner Sponsors',
}

$(document).ready(function () {
    $.get(base_url + '/sponsors/list/').done(function (data) {
        $('#spinner').hide();
        
        sponsors = data.spons;
        sponsors.forEach(function (type) {
            type.sponsors.forEach(function (sponsor) {
                console.log(JSON.stringify(sponsor, null, 2));
                sponsors_html.innerHTML += ` 
                    <div class='sponsor'>
                        <img src='/${sponsor.pic}'>
                        <div class='details'>
                            <h2>${sponsor.name}</h2>
                            <p class='body'>${sponsor.details}</p>
                            <p class='contact_no'>${sponsor.contact}</p>
                            <p class='website'><a href='${sponsor.website}'>website</a></p>
                        </div>
                    </div>`;
            })
        })
    })
})

