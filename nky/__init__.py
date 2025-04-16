from .nky import nky


async def setup(bot):
    await bot.add_cog(nky(bot))