; DON'T OPEN THIS FILE WITH NOTEPAD.  If you don't have a preferred text editor, use notepad++ or any other modern text editor.
;
; If you edit example_options.ini, Save-As options.ini
;
; This is the main configuration file for MusicBot.  You will need to edit this file when you setup the bot.
; The bot must be restarted for edits to take effect, but a reload command will be created in the future.
; Currently the bot does not overwrite any settings, but this may change in a future update.


; HOW TO GET VARIOUS IDS:
; http://i.imgur.com/GhKpBMQ.gif
; Enable developer mode (options, settings, appearance), right click the object you want the id of, and click Copy ID
; This works for basically everything you would want the id of (channels and users).  For roles you have to right click a role mention.


[Credentials]
; Put your token here.  Not "secret".  The secret is not the token.
Token = MzcxNTc4NDc1NTQ4NTA4MTYw.DNI2zA.kHc4elmTvOMBuMI6IVLG3VmZT5I
; If you want to use a normal user account instead of a bot account, use these lines instead.
; Comment the token line and uncomment the Email/Password lines.
;Email = bot_discord@email
;Password = bot_discord_password

[Permissions]
; This number should be your id.  It gives you full permissions.  You do not put the bot's id here.  That's silly.
; If you don't know how to get this, scroll up a bit and read the part that says "HOW TO GET VARIOUS IDS"
; If you can't do that for some reason, join the help server (invite in the readme) and type this in chat: !id
; If you still don't understand, watch this https://streamable.com/4w8e and may your respective deity have mercy on your soul.
; I don't want any more "how do I get the OwnerID" questions.
OwnerID = 305341613071269889

[Chat]
; Change this if you don't want commands to trigger another bot
; Example:
;	CommandPrefix = *
; This means the commands you use in chat are *play, *skip, etc.  This explanation exists because it seems no one knows what "prefix" means.
; You do not list commands here.  You do not put "CommandPrefix = *play *queue *np *skip *clear..." etc.  R e a d i n g   c o m p r e h e n s i o n.
CommandPrefix = @

; Restrict the bot to only listen to certain text channels.  Uncomment (remove the ; at the start of the line) and add channel IDs to enable.
; An id looks like this number: 41771983423143930
; To get a channel id, enable Developer Mode in discord (settings, appearance), right click a channel, and click Copy ID.
; Example: BindToChannels = 41000000000000005 41000000000000007
; (Don't use these ids, they won't work)
; This next line is the one you uncomment to use the option:
;
;BindToChannels =
;

; Join a channel on startup.  Multiple channels can be added for multiple servers. Remember, use IDs, not names.
; If both this option and AutoSummon are enabled, this option takes priority.
;
;AutojoinChannels =
;

[MusicBot]
; The starting volume of the bot.  You can use any value from 0.01 to 1.0 but 0.15 is probably fine
DefaultVolume = 0.15

; Only allow whitelisted users to use commands
; Deprecated in favor of permissions
WhiteListCheck = no

; Skips required to skip a song.  Whichever is lower will be used.
; Skip ratio refers to the percent of non-deafened, non-owner users
; in the voice channel needed to skip a song.
SkipsRequired = 4
SkipRatio = 0.5

; If no, delete videos after they've played, if the video
; isn't still in the queue, to avoid redownloading it.
SaveVideos = yes

; Mentions the user who queued a song when the song plays.
NowPlayingMentions = yes

; On start up, if the owner is in a voice channel, join that channel.
AutoSummon = yes

; Play random songs when nothing is queued.
UseAutoPlaylist = yes

; When no one else is in the voice channel, pause the music, and resume when someone joins again.
AutoPause = yes

; Automatically delete messages the bot sends after some time.
DeleteMessages = yes

; Delete the invoking message when DeleteMessages is enabled.  Does nothing when DeleteMessages is disabled.
; Note the bot must have Manage Messages permission in the channel to delete other messages.
DeleteInvoking = no

; Prints extra output in the console and some errors to chat.
; This option is a work in progress, don't expect much.  You might as well just leave it on for now.
DebugMode = no


; DON'T OPEN THIS FILE WITH NOTEPAD.  If you don't have a preferred text editor, use notepad++ or any other modern text editor.
;
; If you edit this file, Save-As permissions.ini
;
;
; Basics:
; - Semicolons are comment characters, any line that starts with one is ignored.
; - Sections headers are permissions groups, they're the lines that have a word in [Brackets].  You can add more for more permissions groups.
; - Options with a semicolon before them will be ignored.
; - Add whatever permissions you want, but always have at least one.
; - Never have an options without a value, i.e. "CommandBlacklist = "
; - [Default] is a special section.  Any user that doesn't get assigned to a group via role or UserList gets assigned to this group.
;
;
; Option info:
;
;    [Groupname]
;    This is the section header.  The word is the name of the group, just name it something appropriate for its permissions.
;
;    CommandWhitelist = command1 command2
;    List of commands users are allowed to use, separated by spaces.  Don't include the prefix, i.e. !  Overrides CommandBlacklist if set.
;
;    CommandBlacklist = command1 command2
;    List if commands users are not allowed to use.  You don't need to use both
;    whitelist and blacklist since blacklist gets overridden.  Just pick one.
;
;    IgnoreNonVoice = command1 command2
;    List of commands that the user is required to be in the same voice channel as the bot to use.
;    For example, if you don't want the user to be able to voteskip songs while not in the voice channel, add skip to this option.
;
;    GrantToRoles = 111222333444555 999888777000111
;    List of ids to automatically grant this group to.  To get the id of a role, use the listids command.
;
;    UserList = 21343341324 321432413214321
;    List of user ids to grant this group to.  This option overrides the role granted by the GrantToRoles option.
;
;    MaxSongLength = 600
;    Maximum length of a song in seconds.  Note: This won't always work if the song data doesn't have duration listed.
;    This doesn't happen often, but youtube, soundcloud, etc work fine though.  This will be fixed in a future update.
;    A value of 0 means unlimited.
;
;    MaxSongs = 5
;    Maximum number of songs a user is allowed to queue. A value of 0 means unlimited.
;
;    MaxPlaylistLength = 10
;    Maximum number of songs a playlist is allowed to have to be queued. A value of 0 means unlimited.
;
;    AllowPlaylists = yes
;    Whether or not the user is allowed to queue entire playlists.
;
;    InstaSkip = no
;    Allows the user to skip a song without having to vote, like the owner.
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


; I've set some example groups, these should be fine.  Just add your roles or users and you should be good to go.

;;;;;;;;;;;;;;;;;;;
;
;  AND HEY.
;  Before you ask any dumb "how do I do this" questions in the help server, you should probably read that big comment I put time
;  into writing for this exact purpose.  It tells you how to use every option.  Your question is probably answered there.
;
;;;;;;;;;;;;;;;;;;;

; This is the fallback group for any users that don't get assigned to another group.  Don't remove/rename this group.
[Default]
CommandWhitelist = play perms queue np skip search id help clean
; CommandBlacklist = 372757798720634891 
IgnoreNonVoice = play skip search
; GrantToRoles = 372757798720634891 
; UserList = 372757798720634891 
MaxSongLength = 1200
MaxSongs = 0
AllowPlaylists = yes
; MaxPlaylistLength = 20
InstaSkip = no

; This group has full permissions.
[MusicMaster] 
; GrantToRoles = 372757798720634891 
; UserList = 372757798720634891 
MaxSongLength = 0
MaxSongs = 0
MaxPlaylistLength = 0
AllowPlaylists = yes
InstaSkip = yes

; This group can't use the blacklist and listids commands, but otherwise has full permissions.
[DJ]
CommandBlacklist = blacklist listids
; GrantToRoles = 372757798720634891 
; UserList = 372757798720634891 
MaxSongLength = 0
MaxSongs = 0
MaxPlaylistLength = 0
AllowPlaylists = yes
InstaSkip = yes

; This group can only use the listed commands, can only use play/skip when in the bot's voice channel,
; can't request songs longer than 3 and a half minutes, and can only request a maximum of 8 songs at a time.
[Limited]
CommandWhitelist = play queue np perms help skip
; CommandBlacklist = 372757798720634891  
IgnoreNonVoice = play skip
; GrantToRoles = 372757798720634891 
MaxSongLength = 210
MaxSongs = 8
AllowPlaylists = yes
InstaSkip = no
