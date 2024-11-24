import discord
import random
from discord.ext import commands

permisos=discord.Intents.default()
permisos.message_content=True


bot=commands.Bot(command_prefix="/",intents=permisos)

IDEAS_ECOLOGICAS = [
    "Usa una botella de agua reutilizable en lugar de comprar botellas de plástico. 🌊",
    "Planta un árbol en tu comunidad para combatir el cambio climático. 🌱",
    "Reduce el consumo de carne por un día a la semana para disminuir tu huella de carbono. 🌍",
    "Apaga las luces y desconecta los dispositivos cuando no los estés usando. 💡",
    "Separa tus residuos en orgánicos, reciclables y no reciclables. ♻️",
    "Usa bolsas reutilizables en lugar de plásticas al hacer tus compras. 🛍️",
    "usa bicicleta para reducir las el uso del transporte. 🚴",
    "Recolecta agua de lluvia para regar tus plantas. 🌧️",
    "Participa en actividades de limpieza de playas, parques o ríos. 🏖️",
    "Reutiliza frascos de vidrio como recipientes para almacenar alimentos o hacer manualidades. 🏺"
]


@bot.event
async def on_ready():
    print(f"El bot llamado {bot.user} esta en linea")
@bot.command()
async def reciclaje(ctx):
    await ctx.send("¡Hola crack!, quieres saber sobre la contaminacion y como evitarla, ¡Mira si dices esto te dare infomacion de lo que eligas!: si pones descomposicion y el material que quieras poner te dare la informacion si esque mi base de datos me lo permite, mira un ejemplo /descomposicion botella de plastico, recuerda que todo va con slash 👍👍😃, si quieres saber que cosas usar para evitar la contaminacion usa ,/usamos, y te dare informacion 👌😎")

@bot.command()
async def descomposicion(ctx,*,objeto:str):
    listaDescomposion={
        "botella de plastico": 500,
        "chicle": 10,
        "vidrio": 5000,
        "tecnopor": 500,
        "carton": 1,
        "metal": 30,
        "papel": 1,
        "tela": 200
    }
    objeto=objeto.lower()
    if objeto in listaDescomposion:
        await ctx.send(f"El objeto llamado: {objeto} tarda en descomponerse aproximadamente {listaDescomposion[objeto]} años")
    else:
        await ctx.send("No tengo informacion al respecto ")

@bot.command()
async def usamos(ctx):
    await ctx.send("Recuerda que siempre es mejor usar bolsos de yute en vez de bolsas de plástico.")
    await ctx.send("https://printperu.pe/productos/wp-content/uploads/2020/01/1111_Mesa-de-trabajo-1-600x578.png")
    
    await ctx.send("Opta por botellas reutilizables en lugar de botellas de plástico desechables. Así reduces los residuos y cuidas el planeta.")
    await ctx.send("https://www.esturirafi.com/wp-content/uploads/2021/03/botella-reutlizable-cual-elegir.jpg")
    
    await ctx.send("Prefiere pajitas de acero inoxidable o bambú. Las de plástico tardan cientos de años en descomponerse.")
    await ctx.send("https://nowasteplace.com/wp-content/uploads/2020/01/pailles-bambou-eco-panda-768x576.jpg")
    
    await ctx.send("Cuando compres alimentos, lleva tus propios recipientes o envases reutilizables.")
    await ctx.send("https://images.surferseo.art/bcfb5a04-c395-4cb4-9719-7dafb55fa78f.jpeg")
    
    await ctx.send("Evita los cubiertos desechables y usa cubiertos de madera, bambú o metal.")
    await ctx.send("https://gangxuan-ecotech.com/wp-content/uploads/2022/09/Bamboo-Cutlery.jpg")
    
    await ctx.send("Si te gusta el café para llevar, lleva tu propio vaso reutilizable. ¡Menos residuos!")
    await ctx.send("https://ordenatucafe.com/wp-content/uploads/2021/11/vaso-termico.jpg.webp")
    
    await ctx.send("Prefiere jabones y champús sólidos en lugar de los líquidos en botellas de plástico.")
    await ctx.send("https://conciencia.eco/wp-content/uploads/2024/06/Barras-de-champu-solido-de-varios-colores-y-aromas-dispuestas-en-una-jabonera-de-madera-en-un-bano-elegante.jpg")
    
    await ctx.send("Pequeñas acciones como estas ayudan a proteger nuestro hogar, la Tierra. ¡Sé parte del cambio!")

@bot.command()
async def idea(ctx):
    idea = random.choice(IDEAS_ECOLOGICAS)
    await ctx.send(f"🌿 Aquí tienes una idea ecológica: {idea}")

@bot.command()
async def youtube(ctx):
    await ctx.send("Quieres conocer canales de youtube sobre la contaminacion? 😎👌 aca hay algunos:")
    await ctx.send("Vivir sin plastico: https://www.youtube.com/c/Vivirsinplástico/videos")
    await ctx.send("EcologiaVerde: https://www.youtube.com/@EcologiaVerde/videos")
    await ctx.send("SoyAHORA: https://www.youtube.com/@SoyAHORA/videos")
    
bot.run("TOKEN")
