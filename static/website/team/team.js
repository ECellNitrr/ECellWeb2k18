function show_with_pic(target, members) {
    members.forEach(function (member) {
        var member_html = `
            <div class="member">
                <img src="https://ecellnitrr.herokuapp.com/${member.url}">
                <div class="description">
                    <h4 class="name">${member.name}</h4>
                </div>
            </div>
        `
        target.append(member_html)
    })
}

function draw_as_table(target, members) {
    members.forEach(function (member) {
        var member_html = `
            <div class="member_table">
                <h4 class="name">${member.name}</h4>
            </div>
        `
        target.append(member_html)
    })
}

$(function () {

    var director = $('#director')
    var overall_co = $('#overall-co')
    var head_co = $('#head-co')
    var managers = $('#managers')
    var executives = $('#executives')
    var head_career_dev = $('#head_career-dev')
    var faculty_incharge = $('#faculty_incharge')

    $.get('https://ecellnitrr.herokuapp.com/team/list').then(function (data) {
        // get the data of the given member_type
        function dataOfFaculty(mtype){
            return data.Faculty.filter(val=>val.member_type==mtype)
        }
        function dataOfStudent(mtype){
            return data.Student.filter(val=>val.member_type==mtype)
        }
        
        console.log(dataOfFaculty('Dir'));
        show_with_pic(director, dataOfFaculty('Dir'))
        show_with_pic(head_career_dev, dataOfFaculty('HCD'))
        show_with_pic(faculty_incharge, dataOfFaculty('Fclty'))
        show_with_pic(head_co, dataOfStudent('HC'))
        show_with_pic(overall_co, dataOfStudent('OC'))
        draw_as_table(managers, dataOfStudent('MNG'))
        draw_as_table(executives, dataOfStudent('EXEC'))
    })

})