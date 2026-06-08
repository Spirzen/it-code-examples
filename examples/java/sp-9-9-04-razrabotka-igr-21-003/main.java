   package com.example.structuremod;

   import net.fabricmc.fabric.api.command.v2.CommandRegistrationCallback;
   import net.minecraft.block.Blocks;
   import net.minecraft.server.command.ServerCommandSource;
   import net.minecraft.text.Text;
   import net.minecraft.util.math.BlockPos;
   import com.mojang.brigadier.CommandDispatcher;
   import com.mojang.brigadier.arguments.IntegerArgumentType;
   import static net.minecraft.server.command.CommandManager.*;

   public class PyramidCommand {
       public static void register() {
           CommandRegistrationCallback.EVENT.register((dispatcher, registryAccess, environment) ->
               dispatcher.register(literal("structure")
                   .then(literal("pyramid")
                       .then(argument("size", IntegerArgumentType.integer(1, 32))
                           .executes(context -> {
                               ServerCommandSource source = context.getSource();
                               int size = IntegerArgumentType.getInteger(context, "size");
                               BlockPos origin = source.getPosition().add(2, 0, 2).toImmutable();
                               buildPyramid(source.getWorld(), origin, size);
                               source.sendFeedback(() -> Text.literal("Пирамида " + size + "×" + size + " построена."), false);
                               return 1;
                           })
                       )
                   )
               )
           );
       }

       private static void buildPyramid(net.minecraft.world.World world, BlockPos origin, int size) {
           for (int layer = 0; layer < size; layer++) {
               int side = size - layer;
               int y = origin.getY() + layer;
               for (int x = 0; x < side; x++) {
                   for (int z = 0; z < side; z++) {
                       BlockPos pos = origin.add(x, y, z);
                       world.setBlockState(pos, Blocks.SANDSTONE.getDefaultState(), 3);
                   }
               }
           }
       }
   }
