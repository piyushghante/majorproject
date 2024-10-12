import streamlit as st
import streamlit.components.v1 as components

def connect_metamask_ui():
    html_code = """
    <html>
    <body>
        <button id="connectButton" style="background-color: #f6851b; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
            Connect to MetaMask
        </button>
        <p id="status"></p>
        <script src="https://cdn.ethers.io/lib/ethers-5.2.umd.min.js" type="application/javascript"></script>
        <script>
            const connectButton = document.getElementById('connectButton');
            const statusText = document.getElementById('status');

            connectButton.addEventListener('click', async () => {
                if (typeof window.ethereum !== 'undefined') {
                    try {
                        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                        const account = accounts[0];
                        statusText.innerText = `Connected Account: ${account}`;

                        // Send the account address to the Streamlit app
                        window.parent.postMessage({ type: 'FROM_META_MASK', account: account }, '*');
                    } catch (error) {
                        console.error("Error connecting to MetaMask", error);
                        statusText.innerText = 'Connection failed';
                    }
                } else {
                    statusText.innerText = 'MetaMask is not installed';
                }
            });

            window.addEventListener('message', (event) => {
                if (event.data.type === 'FROM_META_MASK') {
                    const account = event.data.account;
                    document.getElementById('status').innerText = `MetaMask Account: ${account}`;
                }
            });
        </script>
    </body>
    </html>
    """
    
    components.html(html_code, height=300)
