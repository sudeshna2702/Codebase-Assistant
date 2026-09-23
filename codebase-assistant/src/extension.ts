// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
// For getting custom sidebarprovider 
import { SidebarProvider } from './frontend/sidebarProvider';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "codebase-assistant" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable1 = vscode.commands.registerCommand('codebase-assistant.hi', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hi! I am ur codebase-assistant!');
	});

	context.subscriptions.push(disposable1);

	// For getting the file names from folders 
	const disposable2 = vscode.commands.registerCommand('codebase-assistant.selectFileORFolder',async () => {
		// Custom Function 
		// vscode.window.showInformationMessage('Hi! I am ur codebase-assistant!');
		const folder = await vscode.window.showOpenDialog({
			canSelectFiles: false,
			canSelectFolders: true,
			canSelectMany: false
		});

		if(!folder || folder.length <= 0)
		{
			return;
		} 

		// As this is indeed a system call this will take a good amount of time.
		await printFolder(folder[0]);
	});

	context.subscriptions.push(disposable2);

	// The real deal - communicating with the sidebar
	const sidebarProvider = new SidebarProvider();

	context.subscriptions.push(
	vscode.window.registerWebviewViewProvider(
		"codebaseAssistant.sidebar",
		sidebarProvider
	)
	);

}

async function printFolder(folder: vscode.Uri) : Promise<void>
{
	// Extract all the files and folders from the chosen folder
	const entries = await vscode.workspace.fs.readDirectory(folder);

	// Each entry stores the name 
    for (const [name, type] of entries) {

        const uri = vscode.Uri.joinPath(folder, name);

        if (type === vscode.FileType.File) {
			// fsPath to get the path
			vscode.window.showInformationMessage(uri.fsPath);
			// vscode.window.showInputBox();
            console.log(uri.fsPath);

        } else if (type === vscode.FileType.Directory) {

            await printFolder(uri);
        }
    }
}


// This method is called when your extension is deactivated
export function deactivate() {
	console.log("Extension has been deactivated!!!");
}
