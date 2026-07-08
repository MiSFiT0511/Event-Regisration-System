let participants = [];

const form = document.getElementById("registrationForm");
const table = document.getElementById("participantTable");
const message = document.getElementById("message");

form.addEventListener("submit", function(event){

    event.preventDefault();

    let name = document.getElementById("name").value.trim();
    let age = document.getElementById("age").value;
    let email = document.getElementById("email").value.trim();

    if(name === ""){
        message.style.color = "red";
        message.innerHTML = "Name cannot be empty";
        return;
    }

    if(age < 18 || age > 100){
        message.style.color = "red";
        message.innerHTML = "Age must be between 18 and 100";
        return;
    }

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

    if(!email.match(emailPattern)){
        message.style.color = "red";
        message.innerHTML = "Invalid Email";
        return;
    }

    participants.push({
        name:name,
        age:age,
        email:email
    });

    displayParticipants();

    message.style.color = "green";
    message.innerHTML = "Participant Registered Successfully!";

    form.reset();

});

function displayParticipants(){

    table.innerHTML = "";

    for(let i=0;i<participants.length;i++){

        table.innerHTML += `
        <tr>
            <td>${participants[i].name}</td>
            <td>${participants[i].age}</td>
            <td>${participants[i].email}</td>
        </tr>
        `;
    }

}