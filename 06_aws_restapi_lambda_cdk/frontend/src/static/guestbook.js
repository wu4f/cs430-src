"use strict";

// fill in your API Gateway endpoint here
const baseApiUrl = "<FMI>";

/** Display the guestbook entries
 *
 *  Builds up the webpage by manipulating the DOM.
 *  Clears the children of the div with the id "entries", then adds the new entries
 *  to it. We call this to initialize the page and update when entries are added.
 */
const viewEntries = entries => {
  const entriesNode = document.getElementById("entries");

  while (entriesNode.firstChild) {
    entriesNode.firstChild.remove();
  }

  entries.map(entry => {
    const nameAndEmail = document.createTextNode(
      entry.name + " <" + entry.email + ">"
    );
    const signedOn = document.createTextNode("signed on " + entry.date);
    const message = document.createTextNode(entry.message);
    const br = document.createElement("br");
    const br2 = document.createElement("br");

    const p = document.createElement("p");
    p.classList.add("entry");
    p.appendChild(nameAndEmail);
    p.appendChild(br);
    p.appendChild(signedOn);
    p.appendChild(br2);
    p.appendChild(message);

    entriesNode.appendChild(p);
  });
};

/** Get the form field values and POST them to the REST API
 *
 *  We send the API JSON and expect the updated entries
 *  in response as JSON.
 *  Display the entries on the page once they arrive.
 */
const sign = async () => {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  const response = await fetch(baseApiUrl + "entry", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "POST",
    body: JSON.stringify({ name: name, email: email, message: message })
  });
  const gbentries = await response.json();
  viewEntries(gbentries);
};

/** GET the guestbook entries from the REST API
 *
 *  Display them on the page once they arrive.
 */
const getEntries = async () => {
  const response = await fetch(baseApiUrl + "entries", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    method: "GET"
  });
  const gbentries = await response.json();
  viewEntries(gbentries);
};

// initialize the entries when a new guest arrives
getEntries();
