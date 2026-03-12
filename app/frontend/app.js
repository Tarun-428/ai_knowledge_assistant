// const API = "http://localhost:8000"

// let history = []

// /* ===========================
//    TOKEN + CONVERSATION SETUP
// =========================== */

// function getToken(){
//     return localStorage.getItem("token")
// }

// /* ===========================
//    LOGIN PROTECTION
// =========================== */

// const token = localStorage.getItem("token")

// if(window.location.pathname === "/chat-ui" && !token){
//     window.location="/login"
// }

// let conversationId = localStorage.getItem("conversation_id")

// if(!conversationId){
//     conversationId = crypto.randomUUID()
//     localStorage.setItem("conversation_id", conversationId)
// }

// /* ===========================
//    PAGE INIT
// =========================== */

// document.addEventListener("DOMContentLoaded", () => {

//     const loginBtn = document.getElementById("loginBtn")
//     const registerBtn = document.getElementById("registerBtn")
//     const uploadBtn = document.getElementById("uploadBtn")
//     const sendBtn = document.getElementById("sendBtn")

//     if(loginBtn) loginBtn.addEventListener("click", loginUser)
//     if(registerBtn) registerBtn.addEventListener("click", registerUser)
//     if(uploadBtn) uploadBtn.addEventListener("click", uploadFile)
//     if(sendBtn) sendBtn.addEventListener("click", askAI)

//     const questionInput = document.getElementById("question")

//     if(questionInput){
//         questionInput.addEventListener("keydown",(e)=>{
//             if(e.key==="Enter"){
//                 e.preventDefault()
//                 askAI()
//             }
//         })
//     }
// })

// /* ===========================
//    LOGIN
// =========================== */

// async function loginUser(){

//     const email = document.getElementById("email").value
//     const password = document.getElementById("password").value

//     const res = await fetch(API+"/auth/login",{
//         method:"POST",
//         headers:{
//             "Content-Type":"application/json"
//         },
//         body:JSON.stringify({
//             email:email,
//             password:password
//         })
//     })

//     const data = await res.json()

//     if(data.access_token){

//         localStorage.setItem("token",data.access_token)

//         conversationId = crypto.randomUUID()
//         localStorage.setItem("conversation_id",conversationId)

//         window.location="/chat-ui"

//     }else{
//         alert("Login failed")
//     }
// }

// /* ===========================
//    REGISTER
// =========================== */

// async function registerUser(){

//     const username=document.getElementById("username").value
//     const email=document.getElementById("email").value
//     const password=document.getElementById("password").value
//     const role=document.getElementById("role").value

//     const res=await fetch(API+"/auth/register",{

//         method:"POST",

//         headers:{
//             "Content-Type":"application/json"
//         },

//         body:JSON.stringify({
//             username:username,
//             email:email,
//             password:password,
//             role:role
//         })

//     })

//     if(res.ok){
//         alert("Account created")
//         window.location="/login"
//     }else{
//         alert("Registration failed")
//     }
// }

// /* ===========================
//    FILE UPLOAD
// =========================== */

// async function uploadFile(){

//     const file=document.getElementById("fileInput").files[0]
//     const uploadBtn=document.getElementById("uploadBtn")
//     const status=document.getElementById("uploadStatus")

//     if(!file){
//         alert("Select a file first")
//         return
//     }

//     uploadBtn.disabled=true
//     uploadBtn.innerText="Uploading..."

//     status.innerHTML="Uploading file..."

//     const formData=new FormData()
//     formData.append("file",file)

//     try{

//         const res=await fetch(API+"/files/documents/upload",{

//             method:"POST",

//             headers:{
//                 "Authorization":"Bearer "+getToken()
//             },

//             body:formData
//         })

//         if(res.ok){
//             status.innerText="Upload completed ✔"
//         }else{
//             status.innerText="Upload failed"
//         }

//     }catch{
//         status.innerText="Upload error"
//     }

//     uploadBtn.disabled=false
//     uploadBtn.innerText="Upload File"
// }

// /* ===========================
//    ASK AI (STREAMING)
// =========================== */

// async function askAI(){

//     const input=document.getElementById("question")
//     const chatBox=document.getElementById("chatBox")
//     const sendBtn=document.getElementById("sendBtn")

//     const question=input.value.trim()

//     if(!question) return

//     /* show user message */

//     chatBox.innerHTML+=`<div class="user">${question}</div>`

//     input.value=""
//     sendBtn.disabled=true

//     /* create assistant bubble */

//     const aiDiv=document.createElement("div")
//     aiDiv.className="ai"
//     aiDiv.innerHTML=`<span class="typing"></span>`

//     chatBox.appendChild(aiDiv)
//     chatBox.scrollTop=chatBox.scrollHeight

//     const typingSpan=aiDiv.querySelector(".typing")

//     try{

//         const response=await fetch(API+"/chat/stream",{

//             method:"POST",

//             headers:{
//                 "Content-Type":"application/json",
//                 "Authorization":"Bearer "+getToken()
//             },

//             body:JSON.stringify({
//                 question:question,
//                 conversation_id:conversationId
//             })

//         })

//         const reader=response.body.getReader()
//         const decoder=new TextDecoder()

//         let result=""

//         while(true){

//             const {done,value}=await reader.read()

//             if(done) break

//             const chunk=decoder.decode(value)
//             const lines=chunk.split("\n")

//             for(const line of lines){

//                 if(line.startsWith("data: ")){

//                     const token=line.replace("data: ","")

//                     if(token==="[DONE]"){
//                         sendBtn.disabled=false
//                         return
//                     }

//                     result+=token
//                     typingSpan.innerText=result

//                     chatBox.scrollTop=chatBox.scrollHeight
//                 }
//             }
//         }

//         history.push({role:"user",content:question})
//         history.push({role:"assistant",content:result})

//     }catch(error){

//         typingSpan.innerText="Error generating answer"
//         sendBtn.disabled=false
//     }
// }

// /* ===========================
//    LOGOUT
// =========================== */

// function logout(){

//     localStorage.removeItem("token")
//     localStorage.removeItem("conversation_id")

//     window.location="/login"
// }

const API = "http://localhost:8000"

let history = []

/* ===========================
   TOKEN + CONVERSATION SETUP
=========================== */

function getToken() {
    return localStorage.getItem("token")
}

/* ===========================
   LOGIN PROTECTION
=========================== */

const token = localStorage.getItem("token")

if (window.location.pathname === "/chat-ui" && !token) {
    window.location = "/login"
}

let conversationId = localStorage.getItem("conversation_id")

if (!conversationId) {
    conversationId = crypto.randomUUID()
    localStorage.setItem("conversation_id", conversationId)
}

/* ===========================
   PAGE INIT
=========================== */

document.addEventListener("DOMContentLoaded", () => {

    const loginBtn = document.getElementById("loginBtn")
    const registerBtn = document.getElementById("registerBtn")
    const uploadBtn = document.getElementById("uploadBtn")
    const sendBtn = document.getElementById("sendBtn")

    if (loginBtn) loginBtn.addEventListener("click", loginUser)
    if (registerBtn) registerBtn.addEventListener("click", registerUser)
    if (uploadBtn) uploadBtn.addEventListener("click", uploadFile)
    if (sendBtn) sendBtn.addEventListener("click", askAI)

    /* ENTER key for chat */
    const questionInput = document.getElementById("question")

    if (questionInput) {
        questionInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault()
                askAI()
            }
        })
    }

    /* ENTER key for login form */
    const loginForm = document.getElementById("loginForm")

    if (loginForm) {
        loginForm.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault()
                loginUser()
            }
        })
    }

    /* ENTER key for register form */
    const registerForm = document.getElementById("registerForm")

    if (registerForm) {
        registerForm.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault()
                registerUser()
            }
        })
    }

})

/* ===========================
   LOGIN
=========================== */

async function loginUser() {

    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const res = await fetch(API + "/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    })

    const data = await res.json()

    if (data.access_token) {

        localStorage.setItem("token", data.access_token)

        conversationId = crypto.randomUUID()
        localStorage.setItem("conversation_id", conversationId)

        window.location = "/chat-ui"

    } else {
        alert("Login failed")
    }
}



async function registerUser() {

    const username = document.getElementById("username").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const role = document.getElementById("role").value

    const res = await fetch(API + "/auth/register", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username: username,
            email: email,
            password: password,
            role: role
        })

    })

    if (res.ok) {
        alert("Account created")
        window.location = "/login"
    } else {
        alert("Registration failed")
    }
}


async function uploadFile() {

    const file = document.getElementById("fileInput").files[0]
    const uploadBtn = document.getElementById("uploadBtn")
    const status = document.getElementById("uploadStatus")

    if (!file) {
        alert("Select a file first")
        return
    }

    uploadBtn.disabled = true
    uploadBtn.innerText = "Uploading..."

    status.innerHTML = "Uploading file..."

    const formData = new FormData()
    formData.append("file", file)

    try {

        const res = await fetch(API + "/files/documents/upload", {

            method: "POST",

            headers: {
                "Authorization": "Bearer " + getToken()
            },

            body: formData
        })

        if (res.ok) {
            status.innerText = "Upload completed ✔"
        } else {
            status.innerText = "Upload failed"
        }

    } catch {
        status.innerText = "Upload error"
    }

    uploadBtn.disabled = false
    uploadBtn.innerText = "Upload File"
}

/* ===========================
   CHAT STREAMING
=========================== */

async function askAI() {

    const input = document.getElementById("question")
    const chatBox = document.getElementById("chatBox")
    const sendBtn = document.getElementById("sendBtn")

    const question = input.value.trim()

    if (!question) return

    /* show user message */

    chatBox.innerHTML += `<div class="user">${question}</div>`

    input.value = ""
    sendBtn.disabled = true

    /* assistant bubble */

    const aiDiv = document.createElement("div")
    aiDiv.className = "ai"
    aiDiv.innerHTML = `<span class="typing"></span>`

    chatBox.appendChild(aiDiv)

    const typingSpan = aiDiv.querySelector(".typing")

    scrollChat()

    try {

        const response = await fetch(API + "/chat/stream", {

            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + getToken()
            },

            body: JSON.stringify({
                question: question,
                conversation_id: conversationId
            })
        })

        const reader = response.body.getReader()
        const decoder = new TextDecoder()

        let buffer = ""
        let result = ""

        while (true) {

            const { done, value } = await reader.read()

            if (done) break

            buffer += decoder.decode(value, { stream: true })

            const parts = buffer.split("\n\n")
            buffer = parts.pop()

            for (const part of parts) {
                if (!part.startsWith("data:")) continue;

                // 1. Get the raw string after "data: " 
                const rawData = part.substring(5).trim();

                if (rawData === "[DONE]") {
                    sendBtn.disabled = false;
                    return;
                }

                try {
                    // 2. Parse the JSON to get the EXACT token (preserving spaces/newlines)
                    const parsed = JSON.parse(rawData);
                    const token = parsed.token;

                    result += token;

                    // 3. Use textContent for performance, CSS will handle the layout
                    typingSpan.textContent = result;

                    scrollChat();
                } catch (e) {
                    console.error("Error parsing SSE data", e);
                }
            }
        }

        history.push({ role: "assistant", content: result })

    } catch (error) {

        typingSpan.innerText = "Error generating answer"
        sendBtn.disabled = false
    }
}



/* ===========================
   CHAT SCROLL
=========================== */

function scrollChat() {

    const chatBox = document.getElementById("chatBox")

    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight
    }
}

/* ===========================
   LOGOUT
=========================== */

function logout() {

    localStorage.removeItem("token")
    localStorage.removeItem("conversation_id")

    window.location = "/login"
}

