# **Discord Server Cloner**

**Clone your Discord servers effortlessly with this powerful script!** Whether you're setting up a new server or migrating content, this script enables you to replicate roles, channels, emojis, and more between servers with ease.

## **📜 Features**

- **Roles**: Clone roles from one server to another.
- **Channels**: Clone text and voice channels, including their permissions and categories.
- **Emojis**: Transfer custom emojis between servers.
- **Guild Icon**: Clone the server icon.
- **Everything**: Clone all of the above in one go.

## **🔧 Requirements**

1. **Python 3.x**: Ensure you have Python 3.x installed.
2. **Dependencies**: Install the required packages using the following command:
   ```
   pip install discord.py aioconsole colorama
   ```

## **🚀 Setup and Usage**

1. **Prepare Your Environment:**
   - Make sure you have your Discord bot token.
   - Ensure you have the necessary permissions for the bot on both source and destination servers.

2. **Run the Script:**
   - Clone the repository or download the script.
   - Execute the script using Python:
     ```
     python ultimate.py
     ```

3. **Input Details:**
   - **Guild ID to Clone From**: Enter the ID of the server you want to clone.
   - **Guild ID to Clone To**: Enter the ID of the server where you want to clone the content.
   - **Bot Token**: Provide your Discord bot token.

4. **Choose What to Clone:**
   - After running the script, you will be prompted to choose what to clone:
     1. **Roles**
     2. **Channels**
     3. **Emojis**
     4. **Guild Icon**
     5. **Everything**

## **🛠️ How It Works**

The script performs the following actions based on your selection:
- **Delete Existing Roles/Channels/Emojis**: Cleans up the destination server.
- **Create New Roles/Channels/Emojis**: Duplicates the setup from the source server.
- **Edit Guild Icon**: Updates the server icon to match the source server.

## **📁 Output**

- **Console Output**: The script will print messages indicating the status of each operation (e.g., role creation, channel deletion).
- **Error Handling**: Any errors encountered during execution will be displayed in the console.

## **⚠️ Warnings**

- **Permissions**: Ensure the bot has sufficient permissions on both source and destination servers.
- **Rate Limits**: Be mindful of Discord's rate limits to avoid getting rate-limited.
- **Bot Usage**: This script uses a self-bot approach. Make sure you adhere to Discord's Terms of Service.

## **🔗 Links**

- [Discord Developer Portal](https://discord.com/developers/applications) - To create and manage your Discord bot.
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/) - For more information on using the Discord.py library.

Happy cloning! If you have any questions or need support, feel free to reach out.
**Developed by:** ultimate
