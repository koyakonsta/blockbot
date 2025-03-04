import hikari
from arc import GatewayClient

async def get_guild(client: GatewayClient, event: hikari.GuildMessageCreateEvent):
    return event.get_guild() or await client.rest.fetch_guild(event.guild_id)

def role_mention(role_id: hikari.Snowflake | int | str):
    return f"<@&{role_id}>"