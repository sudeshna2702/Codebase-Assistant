import * as vscode from 'vscode';
import sideBarHtml from './sidebarHtml';
import { error } from 'console';

interface serverResponse{
	response: String;
}

export class SidebarProvider implements vscode.WebviewViewProvider{
	private view?: vscode.WebviewView;
	private selectedFolder ?: vscode.Uri;

	// This function will be called when sidebar is created - Mandatory
	resolveWebviewView(webviewView: vscode.WebviewView): void {

		// I am storing my sidebar in this variable
		this.view = webviewView;

		webviewView.webview.options = {
			enableScripts : true
		};

		// This to get the html
		const sidebar_html = sideBarHtml();
		webviewView.webview.html = sidebar_html;

		// This is webview to receive messages from extension 
		webviewView.webview.onDidReceiveMessage(async (text) => {
			vscode.window.showInformationMessage('This is the Message:'+text.command);

			switch(text.command)
			{
				case "generateFolderPicker":
				{
					const folder: vscode.Uri[] | undefined = await vscode.window.showOpenDialog({
						canSelectFiles: false,
						canSelectFolders: true,
						canSelectMany: false
					});

					// Checking is very Important 
					if(!folder || folder.length <= 0)
					{
						return;
					}

					// Assigning to my Global Variable
					this.selectedFolder = folder[0];
					const selectedFolderPath = folder[0].fsPath;

					// Send the folder path to backend 
					try{
						const data = await fetch(
							"http://127.0.0.1:8000/folder",
							{
								method: "post",
								headers: {
									"Content-Type": "application/json"
								},
								body: JSON.stringify({
									folder_path: selectedFolderPath
								})
							}
						);

						const serverMessage : serverResponse = await data.json() as serverResponse;
						vscode.window.showInformationMessage('This is Server Message:'+serverMessage.response);

						// When I got a posotive review make sure to open the QNA section
					
					}
					catch{
						console.log("Server Error:" +error);
					}

					
					break;
				}
				default:
					console.log("Unexpected Input Format");
			}
			// try{
			// 	const data = await fetch(
			// 		"http://127.0.0.1:8000/test",
			// 		{
			// 			method: "post",
			// 			headers: {
			// 				"Content-Type": "application/json"
			// 			},
			// 			body: JSON.stringify({
			// 				message: text.message
			// 			})
			// 		}
			// 	);

			// 	const serverMessage: serverResponse = await data.json() as serverResponse;
			// 	vscode.window.showInformationMessage('This is Server Message:'+serverMessage.response);
			// }
			// catch{
			// 	console.log("Some error happened on fastapi side!");
			// }
		});
	}


};