var db = openDatabase('database.sqlite', '1.0', 'my database', 1024 * 1024);
db.transaction(function (tx) {
tx.executeSql("INSERT INTO agenda VALUES ('"+evento+"','"+descricao+"','"+dia+"')");
});

console.log(valor);


function addEvent(title, desc) {
  if (!globalEventObj[selectedDate.toDateString()]) {
     globalEventObj[selectedDate.toDateString()] = {};
  }
  globalEventObj[selectedDate.toDateString()][title] = desc;
}

function showEvents() {
  let sidebarEvents = document.getElementById("sidebarEvents");
  let objWithDate = globalEventObj[selectedDate.toDateString()];

  sidebarEvents.innerHTML = "";

  if (objWithDate) {
     let eventsCount = 0;
     for (key in globalEventObj[selectedDate.toDateString()]) {
        let eventContainer = document.createElement("div");
        eventContainer.className = "eventCard";

        let eventHeader = document.createElement("div");
        eventHeader.className = "eventCard-header";

        let eventDescription = document.createElement("div");
        eventDescription.className = "eventCard-description";

        eventHeader.appendChild(document.createTextNode(key));
        eventContainer.appendChild(eventHeader);

        eventDescription.appendChild(document.createTextNode(objWithDate[key]));
        eventContainer.appendChild(eventDescription);

        let markWrapper = document.createElement("div");
        markWrapper.className = "eventCard-mark-wrapper";
        let mark = document.createElement("div");
        mark.classList = "eventCard-mark";
        markWrapper.appendChild(mark);
        eventContainer.appendChild(markWrapper);

        sidebarEvents.appendChild(eventContainer);

        eventsCount++;
     }
     let emptyFormMessage = document.getElementById("emptyFormTitle");
     emptyFormMessage.innerHTML = `${eventsCount} evento(s) agora`;
  } else {
     let emptyMessage = document.createElement("div");
     emptyMessage.className = "empty-message";
     emptyMessage.innerHTML = "Não há eventos para esse dia";
     sidebarEvents.appendChild(emptyMessage);
     let emptyFormMessage = document.getElementById("emptyFormTitle");
     emptyFormMessage.innerHTML = "Sem eventos agora";
  }
}