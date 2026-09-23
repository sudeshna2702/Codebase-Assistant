import * as vscode from 'vscode';


export default function sidebarHtml(){
    return `
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">

        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Codebase Assistant</title>
    </head>
    <link rel="stylesheet" href="./styles.css">

    <body>

    <h1>Codebase Assistant</h1>
    <button id="selectFolder">Select Folder</button>
    <div class="QnaSection" style="display:none;">
        <span>
            <input class="Question">
            <button >Ask</button>
        </span>
        <div id="AIResponse"></div>
    </div>
    <script>
        // Get VS Code API to return value to my extension
        const vscode = acquireVsCodeApi();

        document.getElementById("selectFolder").addEventListener("click", ()=>{
            vscode.postMessage({
                command: 'generateFolderPicker',
                message: 'selectFolder'
            });
        });
        // document.getElementById("myBtn").addEventListener("click", ()=>{
        //     vscode.postMessage({
        //         command: 'communicationMessage',
        //         message: 'communication Successful' 
        //     });
        // });
    </script>

    </body>
    </html>
    `;
}