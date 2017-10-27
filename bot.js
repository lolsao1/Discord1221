const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('I am ready!');
});

var commands = {
    r1: 'Be respectful to everyone. All discussions should be kept civil and polite.',
    r2: 'No NSFW/R18+ content please.',
    r3: 'No usage of any slurs that will cause offence to others.',
    r4: 'Profanity is fine. However, avoid using it in excess to the point it makes other members feel uncomfortable.',
    r5: 'Keep ALL discussions in the relevant channel they best belong to.',
    r6: 'This is an exclusively English server. Phrases in other languages or occasional chit-chat in your native is acceptable, but keep it to a limit the only exceptions being the dedicated language rooms.',
    r7: 'Refrain from shitposting in this server.',
    r8: 'Usage of nicknames is permitted in this server. Please do not use any offensive nicknames or denote titles in brackets (i.e [Vice-Captain]) in your nickname. These rules are subject to change at any point of time when deemed fit. If you have any concerns, questions, or suggestions, you can always contact a moderator via use of @Mods  or by messaging any of them privately.',
    faq1: 'For CFW please use https://3ds.guide/',
    help: 'The command explanations are pinned in #faq-room.',
    info: 'This bot was created for the Galaxy Translation server.',
    progress: 'Please check #updates.'
};

client.on('message', message => {
    if (message.content.substr(0, 1) !== '.') {
        return;
    }
    for (var i in commands) {
        if (message.content === '.' + commands[i]) {
            break;
        }
    }
    message.reply(commands[i]);
});



// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
