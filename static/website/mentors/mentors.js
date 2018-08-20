fetch(base_url + '/mentors/list/')
    .then(data => data.json())
    .then(function (data) {

        var mentors = $('.people');
        console.log(data)
        document.querySelector('.people').style.opacity = 1
        document.querySelector('#spinner').remove();

        data.mentors.forEach(function (mentor) {
            console.log(mentor);
            mentors.append(`
                <div>
                    <img class="" src='${mentor.profile_pic}' alt="">
                        <div class="">
                        <h3>${mentor.name}</h3>
                        <h4>${mentor.description}</h4>
                    </div>
                </div>
            `)
        })
    })