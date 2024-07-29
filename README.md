#
# A fatal error has been detected by the Java Runtime Environment:
#
#  EXCEPTION_ACCESS_VIOLATION (0xc0000005) at pc=0x000001bcbdf7fb1a, pid=2448, tid=5664
#
# JRE version: OpenJDK Runtime Environment Microsoft-8035246 (17.0.8+7) (build 17.0.8+7-LTS)
# Java VM: OpenJDK 64-Bit Server VM Microsoft-8035246 (17.0.8+7-LTS, mixed mode, tiered, compressed oops, compressed class ptrs, g1 gc, windows-amd64)
# Problematic frame:
# C  0x000001bcbdf7fb1a
#
# No core dump will be written. Minidumps are not enabled by default on client versions of Windows
#
# If you would like to submit a bug report, please visit:
#   https://aka.ms/minecraftjavacrashes
# The crash happened outside the Java Virtual Machine in native code.
# See problematic frame for where to report the bug.
#

---------------  S U M M A R Y ------------

Command Line: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xss1M -Djava.library.path=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Djna.tmpdir=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dorg.lwjgl.system.SharedLibraryExtractPath=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dio.netty.native.workdir=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dminecraft.launcher.brand=minecraft-launcher -Dminecraft.launcher.version=2.27.19 -Djava.net.preferIPv6Addresses=system -DignoreList=bootstraplauncher,securejarhandler,asm-commons,asm-util,asm-analysis,asm-tree,asm,JarJarFileSystems,client-extra,fmlcore,javafmllanguage,lowcodelanguage,mclanguage,forge-,forge-47.2.20.jar,forge-47.2.20 -DmergeModules=jna-5.10.0.jar,jna-platform-5.10.0.jar -DlibraryDirectory=D:\MINE2024\curseforge\minecraft\Install\libraries --module-path=D:\MINE2024\curseforge\minecraft\Install\libraries/cpw/mods/bootstraplauncher/1.1.2/bootstraplauncher-1.1.2.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/cpw/mods/securejarhandler/2.1.10/securejarhandler-2.1.10.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-commons/9.5/asm-commons-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-util/9.5/asm-util-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-analysis/9.5/asm-analysis-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-tree/9.5/asm-tree-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm/9.5/asm-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/net/minecraftforge/JarJarFileSystems/0.3.19/JarJarFileSystems-0.3.19.jar --add-modules=ALL-MODULE-PATH --add-opens=java.base/java.util.jar=cpw.mods.securejarhandler --add-opens=java.base/java.lang.invoke=cpw.mods.securejarhandler --add-exports=java.base/sun.security.util=cpw.mods.securejarhandler --add-exports=jdk.naming.dns/com.sun.jndi.dns=java.naming -Xmx20096m -Xms256m -Dminecraft.applet.TargetDirectory=D:\MINE2024\curseforge\minecraft\Instances\All the Mods 9 - ATM9 -Dfml.ignorePatchDiscrepancies=true -Dfml.ignoreInvalidMinecraftCertificates=true -Duser.language=en -Duser.country=US -DlibraryDirectory=D:\MINE2024\curseforge\minecraft\Install\libraries -Dlog4j.configurationFile=D:\MINE2024\curseforge\minecraft\Install\assets\log_configs\client-1.12.xml cpw.mods.bootstraplauncher.BootstrapLauncher --username TiozaoDosGames --version forge-47.2.20 --gameDir D:\MINE2024\curseforge\minecraft\Instances\All the Mods 9 - ATM9 --assetsDir D:\MINE2024\curseforge\minecraft\Install\assets --assetIndex 5 --uuid 6057701fee244ab2975baf9dc877ed39 -P_ZTXe3Q-MepsFWVg --clientId NjVjNzUxOGYtMmQ5OS00OWIzLWE0ODEtYWI0YmY3ZTkwNGZk --xuid 2535454040662408 --userType msa --versionType release --width 1024 --height 768 --quickPlayPath D:\MINE2024\curseforge\minecraft\Install\quickPlay\java\1722205879594.json --launchTarget forgeclient --fml.forgeVersion 47.2.20 --fml.mcVersion 1.20.1 --fml.forgeGroup net.minecraftforge --fml.mcpVersion 20230612.114412

Host: AMD Ryzen 5 3400G with Radeon Vega Graphics    , 8 cores, 31G,  Windows 10 , 64 bit Build 19041 (10.0.19041.4597)
Time: Sun Jul 28 22:29:39 2024 Hora Padrão de Buenos Aires elapsed time: 10697.433131 seconds (0d 2h 58m 17s)

---------------  T H R E A D  ---------------

Current thread (0x000001bcf8a284a0):  JavaThread "Render thread" [_thread_in_native, id=5664, stack(0x0000003c25200000,0x0000003c25300000)]

Stack: [0x0000003c25200000,0x0000003c25300000],  sp=0x0000003c252fd7e0,  free space=1013k
Native frames: (J=compiled Java code, j=interpreted, Vv=VM code, C=native code)
C  0x000001bcbdf7fb1a

Java frames: (J=compiled Java code, j=interpreted, Vv=VM code)
J 72102  org.lwjgl.opengl.GL32C.nglMultiDrawElementsBaseVertex(IJIJIJ)V org.lwjgl.opengl@3.3.1+7 (0 bytes) @ 0x000001bc8b03fb03 [0x000001bc8b03faa0+0x0000000000000063]
J 75395 c2 me.jellysquid.mods.sodium.client.render.chunk.DefaultChunkRenderer.executeDrawBatch(Lme/jellysquid/mods/sodium/client/gl/device/CommandList;Lme/jellysquid/mods/sodium/client/gl/tessellation/GlTessellation;Lme/jellysquid/mods/sodium/client/gl/device/MultiDrawBatch;)V embeddium@0.3.14+mc1.20.1 (59 bytes) @ 0x000001bc8af9d174 [0x000001bc8af9cea0+0x00000000000002d4]
J 104850 c2 me.jellysquid.mods.sodium.client.render.SodiumWorldRenderer.drawChunkLayer(Lnet/minecraft/client/renderer/RenderType;Lcom/mojang/blaze3d/vertex/PoseStack;DDD)V embeddium@0.3.14+mc1.20.1 (75 bytes) @ 0x000001bc8ad0c33c [0x000001bc8ad0af60+0x00000000000013dc]
J 104980 c2 net.minecraft.client.renderer.LevelRenderer.m_172993_(Lnet/minecraft/client/renderer/RenderType;Lcom/mojang/blaze3d/vertex/PoseStack;DDDLorg/joml/Matrix4f;)V minecraft@1.20.1 (138 bytes) @ 0x000001bc8b0b5514 [0x000001bc8b0b5260+0x00000000000002b4]
J 104844 c2 net.minecraft.client.renderer.LevelRenderer.m_109599_(Lcom/mojang/blaze3d/vertex/PoseStack;FJZLnet/minecraft/client/Camera;Lnet/minecraft/client/renderer/GameRenderer;Lnet/minecraft/client/renderer/LightTexture;Lorg/joml/Matrix4f;)V minecraft@1.20.1 (4384 bytes) @ 0x000001bc8383af90 [0x000001bc838383c0+0x0000000000002bd0]
j  net.minecraft.client.renderer.GameRenderer.m_109089_(FJLcom/mojang/blaze3d/vertex/PoseStack;)V+701 minecraft@1.20.1
J 104361 c2 net.minecraft.client.renderer.GameRenderer.m_109093_(FJZ)V minecraft@1.20.1 (1067 bytes) @ 0x000001bc8bcff350 [0x000001bc8bcfec20+0x0000000000000730]
J 87498 c2 net.minecraft.client.Minecraft.m_91383_(Z)V minecraft@1.20.1 (1214 bytes) @ 0x000001bc8c594a8c [0x000001bc8c5938c0+0x00000000000011cc]
J 99958% c2 net.minecraft.client.Minecraft.m_91374_()V minecraft@1.20.1 (296 bytes) @ 0x000001bc8b32f33c [0x000001bc8b32f180+0x00000000000001bc]
j  net.minecraft.client.main.Main.main([Ljava/lang/String;)V+1576 minecraft@1.20.1
v  ~StubRoutines::call_stub
j  jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Ljava/lang/reflect/Method;Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;+0 java.base@17.0.8
j  jdk.internal.reflect.NativeMethodAccessorImpl.invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;+133 java.base@17.0.8
J 10203 c1 jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object; java.base@17.0.8 (10 bytes) @ 0x000001bc80c434cc [0x000001bc80c433c0+0x000000000000010c]
J 10228 c1 java.lang.reflect.Method.invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object; java.base@17.0.8 (65 bytes) @ 0x000001bc801ce6c4 [0x000001bc801ce380+0x0000000000000344]
j  net.minecraftforge.fml.loading.targets.CommonLaunchHandler.runTarget(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/ModuleLayer;)V+39 fmlloader@1.20.1-47.2.20
j  net.minecraftforge.fml.loading.targets.CommonLaunchHandler.clientService([Ljava/lang/String;Ljava/lang/ModuleLayer;)V+5 fmlloader@1.20.1-47.2.20
j  net.minecraftforge.fml.loading.targets.CommonClientLaunchHandler.lambda$makeService$0([Ljava/lang/String;Ljava/lang/ModuleLayer;)V+3 fmlloader@1.20.1-47.2.20
j  net.minecraftforge.fml.loading.targets.CommonClientLaunchHandler$$Lambda$1192+0x0000000800643ba8.run()V+12 fmlloader@1.20.1-47.2.20
j  cpw.mods.modlauncher.LaunchServiceHandlerDecorator.launch([Ljava/lang/String;Ljava/lang/ModuleLayer;)V+11 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.LaunchServiceHandler.launch(Ljava/lang/String;[Ljava/lang/String;Ljava/lang/ModuleLayer;Lcpw/mods/modlauncher/TransformingClassLoader;Lcpw/mods/modlauncher/LaunchPluginHandler;)V+58 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.LaunchServiceHandler.launch(Lcpw/mods/modlauncher/ArgumentHandler;Ljava/lang/ModuleLayer;Lcpw/mods/modlauncher/TransformingClassLoader;Lcpw/mods/modlauncher/LaunchPluginHandler;)V+21 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.Launcher.run([Ljava/lang/String;)V+307 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.Launcher.main([Ljava/lang/String;)V+78 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.BootstrapLaunchConsumer.accept([Ljava/lang/String;)V+1 cpw.mods.modlauncher@10.0.9
j  cpw.mods.modlauncher.BootstrapLaunchConsumer.accept(Ljava/lang/Object;)V+5 cpw.mods.modlauncher@10.0.9
j  cpw.mods.bootstraplauncher.BootstrapLauncher.main([Ljava/lang/String;)V+515 cpw.mods.bootstraplauncher@1.1.2
v  ~StubRoutines::call_stub

siginfo: EXCEPTION_ACCESS_VIOLATION (0xc0000005), reading address 0x0000000000af5b40


Register to memory mapping:

RIP=0x000001bcbdf7fb1a points into unknown readable memory: 0f b7 3e 89 38 0f
RAX=0x000001c0fd2d7dac points into unknown readable memory: 22 7f 00 00
RBX=0x000001bcbdea0000 points into unknown readable memory: 0x000001bcc4da9430 | 30 94 da c4 bc 01 00 00
RCX=0x0000000000046248 is an unknown value
RDX=0x000001bead692044 points into unknown readable memory: 01 00 00 00
RSP=0x0000003c252fd7e0 is pointing into the stack for thread: 0x000001bcf8a284a0
RBP=0x000001bead693048 points into unknown readable memory: 0x000002ad000002ac | ac 02 00 00 ad 02 00 00
RSI=0x0000000000af5b40 is an unknown value
RDI=0x000000000015eb68 is an unknown value
R8 =0x000001bead692040 points into unknown readable memory: 0x0000000100000000 | 00 00 00 00 01 00 00 00
R9 =0x0000000000000402 is an unknown value
R10=0x000001bcbdf1ef38 points into unknown readable memory: 0x0000000000046248 | 48 62 04 00 00 00 00 00
R11=0x000001bead693048 points into unknown readable memory: 0x000002ad000002ac | ac 02 00 00 ad 02 00 00
R12=0x000001bead692040 points into unknown readable memory: 0x0000000100000000 | 00 00 00 00 01 00 00 00
R13=0x000000000000f078 is an unknown value
R14=0x0 is NULL
R15=0x0 is NULL


Registers:
RAX=0x000001c0fd2d7dac, RBX=0x000001bcbdea0000, RCX=0x0000000000046248, RDX=0x000001bead692044
RSP=0x0000003c252fd7e0, RBP=0x000001bead693048, RSI=0x0000000000af5b40, RDI=0x000000000015eb68
R8 =0x000001bead692040, R9 =0x0000000000000402, R10=0x000001bcbdf1ef38, R11=0x000001bead693048
R12=0x000001bead692040, R13=0x000000000000f078, R14=0x0000000000000000, R15=0x0000000000000000
RIP=0x000001bcbdf7fb1a, EFLAGS=0x0000000000010206

Top of Stack: (sp=0x0000003c252fd7e0)
0x0000003c252fd7e0:   0000000000000000 000001bcc48a5c90
0x0000003c252fd7f0:   000001bcbdea0000 0000000000000402
0x0000003c252fd800:   0000000000000004 00007ff947bde775
0x0000003c252fd810:   0000000000000004 0000000000000000
0x0000003c252fd820:   000000000000f078 000001bcbdea0000
0x0000003c252fd830:   0000000000000000 0000000000000000
0x0000003c252fd840:   0000000000000000 0000000000000000
0x0000003c252fd850:   0000000000000000 000001c0fd2d7dac
0x0000003c252fd860:   0000000000000000 0000000000000000
0x0000003c252fd870:   0000000000000000 000001bcefaba1d8
0x0000003c252fd880:   0000000000000402 000001bcbdf7fac0
0x0000003c252fd890:   000001bcc48a5c90 0000000000000000
0x0000003c252fd8a0:   0000000000000000 0000000000000000
0x0000003c252fd8b0:   0000000000000000 0000000000000001
0x0000003c252fd8c0:   0000000000000001 000001bdd2b4a390
0x0000003c252fd8d0:   000001bcc4977974 00007ff947b6c72e 

Instructions: (pc=0x000001bcbdf7fb1a)
0x000001bcbdf7fa1a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa2a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa3a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa4a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa5a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa6a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa7a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa8a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7fa9a:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0x000001bcbdf7faaa:   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 fe
0x000001bcbdf7faba:   ff ff 80 fa 00 00 48 83 ec 28 48 89 6c 24 20 48
0x000001bcbdf7faca:   89 5c 24 18 48 89 74 24 10 48 89 7c 24 08 48 8b
0x000001bcbdf7fada:   d9 48 8b c2 49 8b e9 49 8b d0 48 8d 2c aa 4c 8b
0x000001bcbdf7faea:   dd 8b 0a 49 ba 38 ef f1 bd bc 01 00 00 41 03 0a
0x000001bcbdf7fafa:   48 83 c2 04 48 be d8 8d ef bd bc 01 00 00 48 8b
0x000001bcbdf7fb0a:   36 48 8b b6 38 03 00 00 48 8d 3c 89 48 8d 34 fe
0x000001bcbdf7fb1a:   0f b7 3e 89 38 0f b7 7e 02 89 78 04 0f b7 7e 04
0x000001bcbdf7fb2a:   89 78 08 0f b7 7e 06 89 78 0c 48 be d8 8d ef bd
0x000001bcbdf7fb3a:   bc 01 00 00 48 8b 36 48 8b b6 68 03 00 00 48 8d
0x000001bcbdf7fb4a:   3c 89 48 8d 34 fe 8b 3e 89 78 10 48 be d8 8d ef
0x000001bcbdf7fb5a:   bd bc 01 00 00 48 8b 36 48 8b b6 98 03 00 00 48
0x000001bcbdf7fb6a:   8d 3c 89 48 8d 34 fe 0f b7 3e f3 0f 2a c7 f3 0f
0x000001bcbdf7fb7a:   11 40 14 0f b7 7e 02 f3 0f 2a c7 f3 0f 11 40 18
0x000001bcbdf7fb8a:   48 be d8 8d ef bd bc 01 00 00 48 8b 36 48 8b b6
0x000001bcbdf7fb9a:   c8 03 00 00 48 8d 3c 89 48 8d 34 fe 0f b7 3e 89
0x000001bcbdf7fbaa:   78 1c 0f b7 7e 02 89 78 20 48 be d8 8d ef bd bc
0x000001bcbdf7fbba:   01 00 00 48 8b 36 48 8b b6 e8 04 00 00 48 8d 3c
0x000001bcbdf7fbca:   89 48 8d 34 fe 0f be 3e d1 e7 ff c7 f3 0f 2a c7
0x000001bcbdf7fbda:   48 bf 00 e8 45 49 f9 7f 00 00 f3 0f 59 07 f3 0f
0x000001bcbdf7fbea:   11 40 24 0f be 7e 01 d1 e7 ff c7 f3 0f 2a c7 48
0x000001bcbdf7fbfa:   bf 00 e8 45 49 f9 7f 00 00 f3 0f 59 07 f3 0f 11
0x000001bcbdf7fc0a:   40 28 0f be 7e 02 d1 e7 ff c7 f3 0f 2a c7 48 bf 


Stack slot to memory mapping:
stack at sp + 0 slots: 0x0 is NULL
stack at sp + 1 slots: 0x000001bcc48a5c90 points into unknown readable memory: 0x0000000000002000 | 00 20 00 00 00 00 00 00
stack at sp + 2 slots: 0x000001bcbdea0000 points into unknown readable memory: 0x000001bcc4da9430 | 30 94 da c4 bc 01 00 00
stack at sp + 3 slots: 0x0000000000000402 is an unknown value
stack at sp + 4 slots: 0x0000000000000004 is an unknown value
stack at sp + 5 slots: 0x00007ff947bde775 nvoglv64.dll
stack at sp + 6 slots: 0x0000000000000004 is an unknown value
stack at sp + 7 slots: 0x0 is NULL


---------------  P R O C E S S  ---------------

Threads class SMR info:
_java_thread_list=0x000001be742a8880, length=104, elements={
0x000001bcf8a284a0, 0x000001bcff760a20, 0x000001bcff7616f0, 0x000001bcff78e550,
0x000001bcff78fe30, 0x000001bcff792eb0, 0x000001bcff7946c0, 0x000001bcff7aa7d0,
0x000001bcff7ab880, 0x000001bcff7b7110, 0x000001bcff86cd60, 0x000001bcff86d270,
0x000001bcc4f950e0, 0x000001bcc4f97960, 0x000001bcc4f93ca0, 0x000001bcc4f93790,
0x000001bcc4f941b0, 0x000001bcc4f95b00, 0x000001bcc4f90f10, 0x000001bcc4f98890,
0x000001bcff86d780, 0x000001bcff86e1a0, 0x000001bcff86a9f0, 0x000001bcc38133b0,
0x000001bcc380f6f0, 0x000001bcc380f1e0, 0x000001bcc380d380, 0x000001bcc4f946c0,
0x000001bcc4f955f0, 0x000001bcc4d39fd0, 0x000001bcc4d358f0, 0x000001bcc4d38680,
0x000001bcc4d37240, 0x000001bcc4d38b90, 0x000001bcc4d395b0, 0x000001bcc4d3a4e0,
0x000001bcc4d33070, 0x000001bcc4d3a9f0, 0x000001bcc380dda0, 0x000001bcc3810110,
0x000001bcea3d01a0, 0x000001bcea3cf780, 0x000001bcea3d1af0, 0x000001bcea3ce340,
0x000001bcc4d36d30, 0x000001bcc4f92860, 0x000001bce9d0f640, 0x000001bcc3812ea0,
0x000001bce9d10a80, 0x000001bcefd4d250, 0x000001bcefd49590, 0x000001bce4af5070,
0x000001bcef6502d0, 0x000001bce4af5580, 0x000001bcefd4d760, 0x000001bce4af5a90,
0x000001bcefd4b900, 0x000001bcefd47c40, 0x000001bcea819840, 0x000001bcefd49fb0,
0x000001bcead93500, 0x000001bd308a6550, 0x000001bd308a5b30, 0x000001bcefd4a4c0,
0x000001bcd2d14ec0, 0x000001bcd2d16300, 0x000001bcead920c0, 0x000001bd2fb63eb0,
0x000001bde1bdf540, 0x000001bcefd47220, 0x000001bcef64ee90, 0x000001bdd2943f40,
0x000001bcd2d16810, 0x000001bcd2d13060, 0x000001bdd2944450, 0x000001bd2fb63490,
0x000001bdd23bd4a0, 0x000001bdd23bd9b0, 0x000001bdd3180ba0, 0x000001bceffb6210,
0x000001bceffb52e0, 0x000001bce9a888e0, 0x000001bdd3180690, 0x000001bd93073a80,
0x000001bcd490f250, 0x000001bcd490e830, 0x000001bcd490c4c0, 0x000001bcd490ed40,
0x000001be74b2edf0, 0x000001be74b2e3d0, 0x000001bdd2e12300, 0x000001bdd2e0f060,
0x000001bdd2e0f570, 0x000001bdd2e104a0, 0x000001bdd2e113d0, 0x000001bdd2e0ff90,
0x000001bead8ad7c0, 0x000001be74b2f300, 0x000001be74b2c570, 0x000001be74b2f810,
0x000001bd930d8b90, 0x000001bdd31810b0, 0x000001bdd3182f10, 0x000001beb1e4ea60
}

Java Threads: ( => current thread )
=>0x000001bcf8a284a0 JavaThread "Render thread" [_thread_in_native, id=5664, stack(0x0000003c25200000,0x0000003c25300000)]
  0x000001bcff760a20 JavaThread "Reference Handler" daemon [_thread_blocked, id=6136, stack(0x0000003c25900000,0x0000003c25a00000)]
  0x000001bcff7616f0 JavaThread "Finalizer" daemon [_thread_blocked, id=12748, stack(0x0000003c25a00000,0x0000003c25b00000)]
  0x000001bcff78e550 JavaThread "Signal Dispatcher" daemon [_thread_blocked, id=12360, stack(0x0000003c25b00000,0x0000003c25c00000)]
  0x000001bcff78fe30 JavaThread "Attach Listener" daemon [_thread_blocked, id=16192, stack(0x0000003c25c00000,0x0000003c25d00000)]
  0x000001bcff792eb0 JavaThread "Service Thread" daemon [_thread_blocked, id=11372, stack(0x0000003c25d00000,0x0000003c25e00000)]
  0x000001bcff7946c0 JavaThread "Monitor Deflation Thread" daemon [_thread_blocked, id=7476, stack(0x0000003c25e00000,0x0000003c25f00000)]
  0x000001bcff7aa7d0 JavaThread "C2 CompilerThread0" daemon [_thread_blocked, id=11628, stack(0x0000003c25f00000,0x0000003c26000000)]
  0x000001bcff7ab880 JavaThread "C1 CompilerThread0" daemon [_thread_blocked, id=16032, stack(0x0000003c26000000,0x0000003c26100000)]
  0x000001bcff7b7110 JavaThread "Sweeper thread" daemon [_thread_blocked, id=9448, stack(0x0000003c26100000,0x0000003c26200000)]
  0x000001bcff86cd60 JavaThread "Common-Cleaner" daemon [_thread_blocked, id=6780, stack(0x0000003c26200000,0x0000003c26300000)]
  0x000001bcff86d270 JavaThread "Notification Thread" daemon [_thread_blocked, id=12412, stack(0x0000003c26400000,0x0000003c26500000)]
  0x000001bcc4f950e0 JavaThread "Thread-0" daemon [_thread_blocked, id=12636, stack(0x0000003c27b00000,0x0000003c27c00000)]
  0x000001bcc4f97960 JavaThread "JNA Cleaner" daemon [_thread_blocked, id=17080, stack(0x0000003c27c00000,0x0000003c27d00000)]
  0x000001bcc4f93ca0 JavaThread "Thread-2" daemon [_thread_in_native, id=20472, stack(0x0000003c27800000,0x0000003c27900000)]
  0x000001bcc4f93790 JavaThread "Thread-3" daemon [_thread_in_native, id=12516, stack(0x0000003c27e00000,0x0000003c27f00000)]
  0x000001bcc4f941b0 JavaThread "Thread-4" daemon [_thread_in_native, id=16952, stack(0x0000003c27f00000,0x0000003c28000000)]
  0x000001bcc4f95b00 JavaThread "Thread-5" daemon [_thread_in_native, id=21820, stack(0x0000003c28000000,0x0000003c28100000)]
  0x000001bcc4f90f10 JavaThread "Thread-6" daemon [_thread_in_native, id=16712, stack(0x0000003c28100000,0x0000003c28200000)]
  0x000001bcc4f98890 JavaThread "Thread-7" daemon [_thread_in_native, id=21072, stack(0x0000003c28200000,0x0000003c28300000)]
  0x000001bcff86d780 JavaThread "Thread-8" daemon [_thread_in_native, id=2508, stack(0x0000003c28300000,0x0000003c28400000)]
  0x000001bcff86e1a0 JavaThread "Thread-9" daemon [_thread_in_native, id=3144, stack(0x0000003c28400000,0x0000003c28500000)]
  0x000001bcff86a9f0 JavaThread "Thread-10" daemon [_thread_in_native, id=13540, stack(0x0000003c28500000,0x0000003c28600000)]
  0x000001bcc38133b0 JavaThread "Timer hack thread" daemon [_thread_blocked, id=14572, stack(0x0000003c27300000,0x0000003c27400000)]
  0x000001bcc380f6f0 JavaThread "Yggdrasil Key Fetcher" daemon [_thread_blocked, id=4052, stack(0x0000003c28800000,0x0000003c28900000)]
  0x000001bcc380f1e0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=14452, stack(0x0000003c28b00000,0x0000003c28c00000)]
  0x000001bcc380d380 JavaThread "DFU cleaning thread" daemon [_thread_blocked, id=14612, stack(0x0000003c28c00000,0x0000003c28d00000)]
  0x000001bcc4f946c0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=17832, stack(0x0000003c29400000,0x0000003c29500000)]
  0x000001bcc4f955f0 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=12744, stack(0x0000003c29500000,0x0000003c29600000)]
  0x000001bcc4d39fd0 JavaThread "Structurize IO Worker #0" daemon [_thread_blocked, id=8556, stack(0x0000003c29600000,0x0000003c29700000)]
  0x000001bcc4d358f0 JavaThread "HttpClient-1-SelectorManager" daemon [_thread_in_native, id=18712, stack(0x0000003c29700000,0x0000003c29800000)]
  0x000001bcc4d38680 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=1508, stack(0x0000003c29a00000,0x0000003c29b00000)]
  0x000001bcc4d37240 JavaThread "JEI Config File Watcher" daemon [_thread_blocked, id=18456, stack(0x0000003c29b00000,0x0000003c29c00000)]
  0x000001bcc4d38b90 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=22232, stack(0x0000003c29c00000,0x0000003c29d00000)]
  0x000001bcc4d395b0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=18148, stack(0x0000003c29d00000,0x0000003c29e00000)]
  0x000001bcc4d3a4e0 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=18508, stack(0x0000003c29e00000,0x0000003c29f00000)]
  0x000001bcc4d33070 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=14588, stack(0x0000003c27600000,0x0000003c27700000)]
  0x000001bcc4d3a9f0 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=18844, stack(0x0000003c28600000,0x0000003c28700000)]
  0x000001bcc380dda0 JavaThread "KubeJS Background Thread" daemon [_thread_blocked, id=17284, stack(0x0000003c2a100000,0x0000003c2a200000)]
  0x000001bcc3810110 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=14708, stack(0x0000003c2a400000,0x0000003c2a500000)]
  0x000001bcea3d01a0 JavaThread "pool-9-thread-1" [_thread_blocked, id=19472, stack(0x0000003c2aa00000,0x0000003c2ab00000)]
  0x000001bcea3cf780 JavaThread "pool-11-thread-1" [_thread_blocked, id=18884, stack(0x0000003c2a300000,0x0000003c2a400000)]
  0x000001bcea3d1af0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=6956, stack(0x0000003c2a000000,0x0000003c2a100000)]
  0x000001bcea3ce340 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=18108, stack(0x0000003c2a200000,0x0000003c2a300000)]
  0x000001bcc4d36d30 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=9864, stack(0x0000003c24f00000,0x0000003c25000000)]
  0x000001bcc4f92860 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=9040, stack(0x0000003c25000000,0x0000003c25100000)]
  0x000001bce9d0f640 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=12060, stack(0x0000003c2ba00000,0x0000003c2bb00000)]
  0x000001bcc3812ea0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=21616, stack(0x0000003c2b100000,0x0000003c2b200000)]
  0x000001bce9d10a80 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=15200, stack(0x0000003c2bb00000,0x0000003c2bc00000)]
  0x000001bcefd4d250 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=10224, stack(0x0000003c2bc00000,0x0000003c2bd00000)]
  0x000001bcefd49590 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=20536, stack(0x0000003c2a900000,0x0000003c2aa00000)]
  0x000001bce4af5070 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=13200, stack(0x0000003c29800000,0x0000003c29900000)]
  0x000001bcef6502d0 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=13140, stack(0x0000003c29900000,0x0000003c29a00000)]
  0x000001bce4af5580 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=1012, stack(0x0000003c2bf00000,0x0000003c2c000000)]
  0x000001bcefd4d760 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=18420, stack(0x0000003c2c000000,0x0000003c2c100000)]
  0x000001bce4af5a90 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=14276, stack(0x0000003c2c100000,0x0000003c2c200000)]
  0x000001bcefd4b900 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=17844, stack(0x0000003c2c200000,0x0000003c2c300000)]
  0x000001bcefd47c40 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=13648, stack(0x0000003c2be00000,0x0000003c2bf00000)]
  0x000001bcea819840 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=8240, stack(0x0000003c2c300000,0x0000003c2c400000)]
  0x000001bcefd49fb0 JavaThread "Discord Rich Presence Timer Thread" [_thread_blocked, id=14680, stack(0x0000003c2c500000,0x0000003c2c600000)]
  0x000001bcead93500 JavaThread "Auto-Sync thread" daemon [_thread_blocked, id=19492, stack(0x0000003c2c400000,0x0000003c2c500000)]
  0x000001bd308a6550 JavaThread "spark-monitoring-thread" daemon [_thread_blocked, id=15740, stack(0x0000003c2c900000,0x0000003c2ca00000)]
  0x000001bd308a5b30 JavaThread "spark-worker-pool-1-thread-1" daemon [_thread_blocked, id=5304, stack(0x0000003c2ca00000,0x0000003c2cb00000)]
  0x000001bcefd4a4c0 JavaThread "Thread-25" daemon [_thread_blocked, id=5596, stack(0x0000003c2cb00000,0x0000003c2cc00000)]
  0x000001bcd2d14ec0 JavaThread "Thread-28" [_thread_blocked, id=18328, stack(0x0000003c2d300000,0x0000003c2d400000)]
  0x000001bcd2d16300 JavaThread "defaultEventExecutor-1-1" [_thread_blocked, id=5908, stack(0x0000003c2d400000,0x0000003c2d500000)]
  0x000001bcead920c0 JavaThread "CullThread" daemon [_thread_blocked, id=4100, stack(0x0000003c2a500000,0x0000003c2a600000)]
  0x000001bd2fb63eb0 JavaThread "Server Pinger #0" daemon [_thread_blocked, id=14072, stack(0x0000003c2ac00000,0x0000003c2ad00000)]
  0x000001bde1bdf540 JavaThread "Thread-29" daemon [_thread_in_native, id=1156, stack(0x0000003c2ae00000,0x0000003c2af00000)]
  0x000001bcefd47220 JavaThread "Netty Client IO #0" daemon [_thread_in_native, id=12776, stack(0x0000003c2af00000,0x0000003c2b000000)]
  0x000001bcef64ee90 JavaThread "Netty Client IO #1" daemon [_thread_in_native, id=7344, stack(0x0000003c2bd00000,0x0000003c2be00000)]
  0x000001bdd2943f40 JavaThread "ComputerCraft-Network-0" daemon [_thread_blocked, id=20756, stack(0x0000003c27000000,0x0000003c27100000)]
  0x000001bcd2d16810 JavaThread "ComputerCraft-Network-1" daemon [_thread_blocked, id=12880, stack(0x0000003c2a600000,0x0000003c2a700000)]
  0x000001bcd2d13060 JavaThread "ComputerCraft-Network-2" daemon [_thread_blocked, id=17368, stack(0x0000003c2c600000,0x0000003c2c700000)]
  0x000001bdd2944450 JavaThread "ComputerCraft-Network-3" daemon [_thread_blocked, id=16492, stack(0x0000003c2d100000,0x0000003c2d200000)]
  0x000001bd2fb63490 JavaThread "Telemetry-Sender-#1" [_thread_blocked, id=15572, stack(0x0000003c2d600000,0x0000003c2d700000)]
  0x000001bdd23bd4a0 JavaThread "pool-16-thread-1" [_thread_blocked, id=20948, stack(0x0000003c2d900000,0x0000003c2da00000)]
  0x000001bdd23bd9b0 JavaThread "pool-8-thread-1" [_thread_blocked, id=8924, stack(0x0000003c2d700000,0x0000003c2d800000)]
  0x000001bdd3180ba0 JavaThread "Java2D Disposer" daemon [_thread_blocked, id=18756, stack(0x0000003c2d800000,0x0000003c2d900000)]
  0x000001bceffb6210 JavaThread "FileSystemWatchService" daemon [_thread_in_native, id=9512, stack(0x0000003c29000000,0x0000003c29100000)]
  0x000001bceffb52e0 JavaThread "Config Lib config file watcher" daemon [_thread_blocked, id=15780, stack(0x0000003c2a700000,0x0000003c2a800000)]
  0x000001bce9a888e0 JavaThread "Flywheel 0" [_thread_blocked, id=5068, stack(0x0000003c2dd00000,0x0000003c2de00000)]
  0x000001bdd3180690 JavaThread "Flywheel 1" [_thread_blocked, id=7684, stack(0x0000003c2de00000,0x0000003c2df00000)]
  0x000001bd93073a80 JavaThread "Worker-Main-692" daemon [_thread_blocked, id=2016, stack(0x0000003c2ab00000,0x0000003c2ac00000)]
  0x000001bcd490f250 JavaThread "JM-texture-64" [_thread_blocked, id=19796, stack(0x0000003c29100000,0x0000003c29200000)]
  0x000001bcd490e830 JavaThread "Worker-Main-945" daemon [_thread_blocked, id=7408, stack(0x0000003c27500000,0x0000003c27600000)]
  0x000001bcd490c4c0 JavaThread "Worker-Main-946" daemon [_thread_blocked, id=16716, stack(0x0000003c28900000,0x0000003c28a00000)]
  0x000001bcd490ed40 JavaThread "JM-texture-67" [_thread_blocked, id=3376, stack(0x0000003c2b600000,0x0000003c2b700000)]
  0x000001be74b2edf0 JavaThread "IO-Worker-991" [_thread_blocked, id=20408, stack(0x0000003c28e00000,0x0000003c28f00000)]
  0x000001be74b2e3d0 JavaThread "IO-Worker-993" [_thread_blocked, id=16500, stack(0x0000003c29200000,0x0000003c29300000)]
  0x000001bdd2e12300 JavaThread "IO-Worker-997" [_thread_blocked, id=4188, stack(0x0000003c2b000000,0x0000003c2b100000)]
  0x000001bdd2e0f060 JavaThread "IO-Worker-999" [_thread_blocked, id=1484, stack(0x0000003c2b200000,0x0000003c2b300000)]
  0x000001bdd2e0f570 JavaThread "IO-Worker-1001" [_thread_blocked, id=5156, stack(0x0000003c2b400000,0x0000003c2b500000)]
  0x000001bdd2e104a0 JavaThread "IO-Worker-1002" [_thread_blocked, id=6412, stack(0x0000003c2b500000,0x0000003c2b600000)]
  0x000001bdd2e113d0 JavaThread "IO-Worker-1003" [_thread_blocked, id=9128, stack(0x0000003c2b700000,0x0000003c2b800000)]
  0x000001bdd2e0ff90 JavaThread "IO-Worker-1004" [_thread_blocked, id=13348, stack(0x0000003c2b800000,0x0000003c2b900000)]
  0x000001bead8ad7c0 JavaThread "IO-Worker-1005" [_thread_blocked, id=4848, stack(0x0000003c2b900000,0x0000003c2ba00000)]
  0x000001be74b2f300 JavaThread "IO-Worker-1006" [_thread_blocked, id=3140, stack(0x0000003c2c800000,0x0000003c2c900000)]
  0x000001be74b2c570 JavaThread "IO-Worker-1007" [_thread_blocked, id=21252, stack(0x0000003c2cc00000,0x0000003c2cd00000)]
  0x000001be74b2f810 JavaThread "IO-Worker-1008" [_thread_blocked, id=20848, stack(0x0000003c2cd00000,0x0000003c2ce00000)]
  0x000001bd930d8b90 JavaThread "Sound engine" daemon [_thread_blocked, id=14828, stack(0x0000003c2ad00000,0x0000003c2ae00000)]
  0x000001bdd31810b0 JavaThread "Chunk Render Task Executor #0" [_thread_blocked, id=12096, stack(0x0000003c26b00000,0x0000003c26c00000)]
  0x000001bdd3182f10 JavaThread "Chunk Render Task Executor #1" [_thread_blocked, id=20236, stack(0x0000003c27a00000,0x0000003c27b00000)]
  0x000001beb1e4ea60 JavaThread "JM-task-70" [_thread_blocked, id=17624, stack(0x0000003c28f00000,0x0000003c29000000)]

Other Threads:
  0x000001bcfc69f8b0 VMThread "VM Thread" [stack: 0x0000003c25800000,0x0000003c25900000] [id=3552]
  0x000001bcffa4ef50 WatcherThread [stack: 0x0000003c26500000,0x0000003c26600000] [id=12340]
  0x000001bcfc58ec40 GCTaskThread "GC Thread#0" [stack: 0x0000003c25300000,0x0000003c25400000] [id=4752]
  0x000001bcbd4c3ca0 GCTaskThread "GC Thread#1" [stack: 0x0000003c26600000,0x0000003c26700000] [id=11660]
  0x000001bcbd447ec0 GCTaskThread "GC Thread#2" [stack: 0x0000003c26700000,0x0000003c26800000] [id=5444]
  0x000001bcbd43f330 GCTaskThread "GC Thread#3" [stack: 0x0000003c26800000,0x0000003c26900000] [id=10040]
  0x000001bcbd583f80 GCTaskThread "GC Thread#4" [stack: 0x0000003c26900000,0x0000003c26a00000] [id=11944]
  0x000001bcbd5a00c0 GCTaskThread "GC Thread#5" [stack: 0x0000003c26a00000,0x0000003c26b00000] [id=12780]
  0x000001bcc50d1910 GCTaskThread "GC Thread#6" [stack: 0x0000003c26c00000,0x0000003c26d00000] [id=13836]
  0x000001bcc3031ca0 GCTaskThread "GC Thread#7" [stack: 0x0000003c26d00000,0x0000003c26e00000] [id=18660]
  0x000001bcf8aac470 ConcurrentGCThread "G1 Main Marker" [stack: 0x0000003c25400000,0x0000003c25500000] [id=21688]
  0x000001bcf8aacd90 ConcurrentGCThread "G1 Conc#0" [stack: 0x0000003c25500000,0x0000003c25600000] [id=7296]
  0x000001bcc50d1420 ConcurrentGCThread "G1 Conc#1" [stack: 0x0000003c26e00000,0x0000003c26f00000] [id=14088]
  0x000001bcf8acd8a0 ConcurrentGCThread "G1 Refine#0" [stack: 0x0000003c25600000,0x0000003c25700000] [id=3944]
  0x000001bcc3423240 ConcurrentGCThread "G1 Refine#1" [stack: 0x0000003c27700000,0x0000003c27800000] [id=9556]
  0x000001bcc5b4cc80 ConcurrentGCThread "G1 Refine#2" [stack: 0x0000003c27900000,0x0000003c27a00000] [id=13716]
  0x000001bcd5d4f480 ConcurrentGCThread "G1 Refine#3" [stack: 0x0000003c28700000,0x0000003c28800000] [id=19356]
  0x000001bce2cea170 ConcurrentGCThread "G1 Refine#4" [stack: 0x0000003c29f00000,0x0000003c2a000000] [id=13084]
  0x000001bcd483a820 ConcurrentGCThread "G1 Refine#5" [stack: 0x0000003c28a00000,0x0000003c28b00000] [id=2032]
  0x000001bcd4096fd0 ConcurrentGCThread "G1 Refine#6" [stack: 0x0000003c2a800000,0x0000003c2a900000] [id=21108]
  0x000001bcefea6b20 ConcurrentGCThread "G1 Refine#7" [stack: 0x0000003c2c700000,0x0000003c2c800000] [id=19368]
  0x000001bcf8ace1e0 ConcurrentGCThread "G1 Service" [stack: 0x0000003c25700000,0x0000003c25800000] [id=20852]

Threads with active compile tasks:

VM state: not at safepoint (normal execution)

VM Mutex/Monitor currently owned by a thread: None

Heap address: 0x0000000318000000, size: 20096 MB, Compressed Oops mode: Zero based, Oop shift amount: 3

CDS archive(s) not mapped
Compressed class space mapped at: 0x0000000800000000-0x0000000840000000, reserved size: 1073741824
Narrow klass base: 0x0000000800000000, Narrow klass shift: 0, Narrow klass range: 0x40000000

GC Precious Log:
 CPUs: 8 total, 8 available
 Memory: 32716M
 Large Page Support: Disabled
 NUMA Support: Disabled
 Compressed Oops: Enabled (Zero based)
 Heap Region Size: 16M
 Heap Min Capacity: 256M
 Heap Initial Capacity: 256M
 Heap Max Capacity: 20096M
 Pre-touch: Disabled
 Parallel Workers: 8
 Concurrent Workers: 2
 Concurrent Refinement Workers: 8
 Periodic GC: Disabled

Heap:
 garbage-first heap   total 15187968K, used 13388808K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 244 young (3997696K), 12 survivors (196608K)
 Metaspace       used 709311K, committed 713152K, reserved 1638400K
  class space    used 141254K, committed 142976K, reserved 1048576K

Heap Regions: E=young(eden), S=young(survivor), O=old, HS=humongous(starts), HC=humongous(continues), CS=collection set, F=free, OA=open archive, CA=closed archive, TAMS=top-at-mark-start (previous, next)
|   0|0x0000000318000000, 0x0000000319000000, 0x0000000319000000|100%| O|  |TAMS 0x0000000319000000, 0x0000000318000000| Untracked 
|   1|0x0000000319000000, 0x000000031a000000, 0x000000031a000000|100%| O|  |TAMS 0x000000031a000000, 0x0000000319000000| Untracked 
|   2|0x000000031a000000, 0x000000031b000000, 0x000000031b000000|100%| O|  |TAMS 0x000000031b000000, 0x000000031a000000| Untracked 
|   3|0x000000031b000000, 0x000000031c000000, 0x000000031c000000|100%| O|  |TAMS 0x000000031c000000, 0x000000031b000000| Untracked 
|   4|0x000000031c000000, 0x000000031d000000, 0x000000031d000000|100%| O|  |TAMS 0x000000031d000000, 0x000000031c000000| Untracked 
|   5|0x000000031d000000, 0x000000031e000000, 0x000000031e000000|100%| O|  |TAMS 0x000000031e000000, 0x000000031d000000| Untracked 
|   6|0x000000031e000000, 0x000000031f000000, 0x000000031f000000|100%| O|  |TAMS 0x000000031f000000, 0x000000031e000000| Untracked 
|   7|0x000000031f000000, 0x0000000320000000, 0x0000000320000000|100%| O|  |TAMS 0x0000000320000000, 0x000000031f000000| Untracked 
|   8|0x0000000320000000, 0x0000000321000000, 0x0000000321000000|100%| O|  |TAMS 0x0000000321000000, 0x0000000320000000| Untracked 
|   9|0x0000000321000000, 0x0000000322000000, 0x0000000322000000|100%| O|  |TAMS 0x0000000322000000, 0x0000000321000000| Untracked 
|  10|0x0000000322000000, 0x0000000323000000, 0x0000000323000000|100%| O|  |TAMS 0x0000000323000000, 0x0000000322000000| Untracked 
|  11|0x0000000323000000, 0x0000000324000000, 0x0000000324000000|100%| O|  |TAMS 0x0000000324000000, 0x0000000323000000| Untracked 
|  12|0x0000000324000000, 0x0000000325000000, 0x0000000325000000|100%| O|  |TAMS 0x0000000325000000, 0x0000000324000000| Untracked 
|  13|0x0000000325000000, 0x0000000326000000, 0x0000000326000000|100%| O|  |TAMS 0x0000000326000000, 0x0000000325000000| Untracked 
|  14|0x0000000326000000, 0x0000000327000000, 0x0000000327000000|100%| O|  |TAMS 0x0000000327000000, 0x0000000326000000| Untracked 
|  15|0x0000000327000000, 0x0000000328000000, 0x0000000328000000|100%| O|  |TAMS 0x0000000328000000, 0x0000000327000000| Untracked 
|  16|0x0000000328000000, 0x0000000329000000, 0x0000000329000000|100%| O|  |TAMS 0x0000000329000000, 0x0000000328000000| Untracked 
|  17|0x0000000329000000, 0x000000032a000000, 0x000000032a000000|100%| O|  |TAMS 0x000000032a000000, 0x0000000329000000| Untracked 
|  18|0x000000032a000000, 0x000000032b000000, 0x000000032b000000|100%| O|  |TAMS 0x000000032b000000, 0x000000032a000000| Untracked 
|  19|0x000000032b000000, 0x000000032c000000, 0x000000032c000000|100%| O|  |TAMS 0x000000032c000000, 0x000000032b000000| Untracked 
|  20|0x000000032c000000, 0x000000032d000000, 0x000000032d000000|100%| O|  |TAMS 0x000000032d000000, 0x000000032c000000| Untracked 
|  21|0x000000032d000000, 0x000000032e000000, 0x000000032e000000|100%| O|  |TAMS 0x000000032e000000, 0x000000032d000000| Untracked 
|  22|0x000000032e000000, 0x000000032f000000, 0x000000032f000000|100%| O|  |TAMS 0x000000032f000000, 0x000000032e000000| Untracked 
|  23|0x000000032f000000, 0x0000000330000000, 0x0000000330000000|100%| O|  |TAMS 0x0000000330000000, 0x000000032f000000| Untracked 
|  24|0x0000000330000000, 0x0000000331000000, 0x0000000331000000|100%| O|  |TAMS 0x0000000331000000, 0x0000000330000000| Untracked 
|  25|0x0000000331000000, 0x0000000332000000, 0x0000000332000000|100%| O|  |TAMS 0x0000000332000000, 0x0000000331000000| Untracked 
|  26|0x0000000332000000, 0x0000000333000000, 0x0000000333000000|100%| O|  |TAMS 0x0000000333000000, 0x0000000332000000| Untracked 
|  27|0x0000000333000000, 0x0000000334000000, 0x0000000334000000|100%| O|  |TAMS 0x0000000334000000, 0x0000000333000000| Untracked 
|  28|0x0000000334000000, 0x0000000335000000, 0x0000000335000000|100%| O|  |TAMS 0x0000000335000000, 0x0000000334000000| Untracked 
|  29|0x0000000335000000, 0x0000000336000000, 0x0000000336000000|100%| O|  |TAMS 0x0000000336000000, 0x0000000335000000| Untracked 
|  30|0x0000000336000000, 0x0000000337000000, 0x0000000337000000|100%| O|  |TAMS 0x0000000337000000, 0x0000000336000000| Untracked 
|  31|0x0000000337000000, 0x0000000338000000, 0x0000000338000000|100%| O|  |TAMS 0x0000000338000000, 0x0000000337000000| Untracked 
|  32|0x0000000338000000, 0x0000000339000000, 0x0000000339000000|100%| O|  |TAMS 0x0000000339000000, 0x0000000338000000| Untracked 
|  33|0x0000000339000000, 0x000000033a000000, 0x000000033a000000|100%| O|  |TAMS 0x000000033a000000, 0x0000000339000000| Untracked 
|  34|0x000000033a000000, 0x000000033b000000, 0x000000033b000000|100%| O|  |TAMS 0x000000033b000000, 0x000000033a000000| Untracked 
|  35|0x000000033b000000, 0x000000033c000000, 0x000000033c000000|100%| O|  |TAMS 0x000000033c000000, 0x000000033b000000| Untracked 
|  36|0x000000033c000000, 0x000000033d000000, 0x000000033d000000|100%| O|  |TAMS 0x000000033d000000, 0x000000033c000000| Untracked 
|  37|0x000000033d000000, 0x000000033e000000, 0x000000033e000000|100%| O|  |TAMS 0x000000033e000000, 0x000000033d000000| Untracked 
|  38|0x000000033e000000, 0x000000033f000000, 0x000000033f000000|100%| O|  |TAMS 0x000000033f000000, 0x000000033e000000| Untracked 
|  39|0x000000033f000000, 0x0000000340000000, 0x0000000340000000|100%| O|  |TAMS 0x0000000340000000, 0x000000033f000000| Untracked 
|  40|0x0000000340000000, 0x0000000341000000, 0x0000000341000000|100%| O|  |TAMS 0x0000000341000000, 0x0000000340000000| Untracked 
|  41|0x0000000341000000, 0x0000000342000000, 0x0000000342000000|100%| O|  |TAMS 0x0000000342000000, 0x0000000341000000| Untracked 
|  42|0x0000000342000000, 0x0000000343000000, 0x0000000343000000|100%| O|  |TAMS 0x0000000343000000, 0x0000000342000000| Untracked 
|  43|0x0000000343000000, 0x0000000344000000, 0x0000000344000000|100%| O|  |TAMS 0x0000000344000000, 0x0000000343000000| Untracked 
|  44|0x0000000344000000, 0x0000000345000000, 0x0000000345000000|100%| O|  |TAMS 0x0000000345000000, 0x0000000344000000| Untracked 
|  45|0x0000000345000000, 0x0000000346000000, 0x0000000346000000|100%| O|  |TAMS 0x0000000346000000, 0x0000000345000000| Untracked 
|  46|0x0000000346000000, 0x0000000347000000, 0x0000000347000000|100%| O|  |TAMS 0x0000000347000000, 0x0000000346000000| Untracked 
|  47|0x0000000347000000, 0x0000000348000000, 0x0000000348000000|100%| O|  |TAMS 0x0000000348000000, 0x0000000347000000| Untracked 
|  48|0x0000000348000000, 0x0000000349000000, 0x0000000349000000|100%| O|  |TAMS 0x0000000349000000, 0x0000000348000000| Untracked 
|  49|0x0000000349000000, 0x000000034a000000, 0x000000034a000000|100%| O|  |TAMS 0x000000034a000000, 0x0000000349000000| Untracked 
|  50|0x000000034a000000, 0x000000034b000000, 0x000000034b000000|100%| O|  |TAMS 0x000000034b000000, 0x000000034a000000| Untracked 
|  51|0x000000034b000000, 0x000000034c000000, 0x000000034c000000|100%| O|  |TAMS 0x000000034c000000, 0x000000034b000000| Untracked 
|  52|0x000000034c000000, 0x000000034d000000, 0x000000034d000000|100%| O|  |TAMS 0x000000034d000000, 0x000000034c000000| Untracked 
|  53|0x000000034d000000, 0x000000034e000000, 0x000000034e000000|100%| O|  |TAMS 0x000000034e000000, 0x000000034d000000| Untracked 
|  54|0x000000034e000000, 0x000000034f000000, 0x000000034f000000|100%| O|  |TAMS 0x000000034f000000, 0x000000034e000000| Untracked 
|  55|0x000000034f000000, 0x0000000350000000, 0x0000000350000000|100%| O|  |TAMS 0x0000000350000000, 0x000000034f000000| Untracked 
|  56|0x0000000350000000, 0x0000000351000000, 0x0000000351000000|100%| O|  |TAMS 0x0000000351000000, 0x0000000350000000| Untracked 
|  57|0x0000000351000000, 0x0000000352000000, 0x0000000352000000|100%| O|  |TAMS 0x0000000352000000, 0x0000000351000000| Untracked 
|  58|0x0000000352000000, 0x0000000353000000, 0x0000000353000000|100%| O|  |TAMS 0x0000000353000000, 0x0000000352000000| Untracked 
|  59|0x0000000353000000, 0x0000000354000000, 0x0000000354000000|100%| O|  |TAMS 0x0000000354000000, 0x0000000353000000| Untracked 
|  60|0x0000000354000000, 0x0000000355000000, 0x0000000355000000|100%| O|  |TAMS 0x0000000355000000, 0x0000000354000000| Untracked 
|  61|0x0000000355000000, 0x0000000356000000, 0x0000000356000000|100%| O|  |TAMS 0x0000000356000000, 0x0000000355000000| Untracked 
|  62|0x0000000356000000, 0x0000000357000000, 0x0000000357000000|100%| O|  |TAMS 0x0000000357000000, 0x0000000356000000| Untracked 
|  63|0x0000000357000000, 0x0000000358000000, 0x0000000358000000|100%| O|  |TAMS 0x0000000358000000, 0x0000000357000000| Untracked 
|  64|0x0000000358000000, 0x0000000359000000, 0x0000000359000000|100%| O|  |TAMS 0x0000000359000000, 0x0000000358000000| Untracked 
|  65|0x0000000359000000, 0x000000035a000000, 0x000000035a000000|100%| O|  |TAMS 0x000000035a000000, 0x0000000359000000| Untracked 
|  66|0x000000035a000000, 0x000000035b000000, 0x000000035b000000|100%| O|  |TAMS 0x000000035b000000, 0x000000035a000000| Untracked 
|  67|0x000000035b000000, 0x000000035c000000, 0x000000035c000000|100%| O|  |TAMS 0x000000035c000000, 0x000000035b000000| Untracked 
|  68|0x000000035c000000, 0x000000035d000000, 0x000000035d000000|100%| O|  |TAMS 0x000000035d000000, 0x000000035c000000| Untracked 
|  69|0x000000035d000000, 0x000000035e000000, 0x000000035e000000|100%| O|  |TAMS 0x000000035e000000, 0x000000035d000000| Untracked 
|  70|0x000000035e000000, 0x000000035f000000, 0x000000035f000000|100%| O|  |TAMS 0x000000035f000000, 0x000000035e000000| Untracked 
|  71|0x000000035f000000, 0x0000000360000000, 0x0000000360000000|100%| O|  |TAMS 0x0000000360000000, 0x000000035f000000| Untracked 
|  72|0x0000000360000000, 0x0000000361000000, 0x0000000361000000|100%| O|  |TAMS 0x0000000361000000, 0x0000000360000000| Untracked 
|  73|0x0000000361000000, 0x0000000362000000, 0x0000000362000000|100%| O|  |TAMS 0x0000000362000000, 0x0000000361000000| Untracked 
|  74|0x0000000362000000, 0x0000000363000000, 0x0000000363000000|100%| O|  |TAMS 0x0000000363000000, 0x0000000362000000| Untracked 
|  75|0x0000000363000000, 0x0000000364000000, 0x0000000364000000|100%| O|  |TAMS 0x0000000364000000, 0x0000000363000000| Untracked 
|  76|0x0000000364000000, 0x0000000365000000, 0x0000000365000000|100%| O|  |TAMS 0x0000000365000000, 0x0000000364000000| Untracked 
|  77|0x0000000365000000, 0x0000000366000000, 0x0000000366000000|100%| O|  |TAMS 0x0000000366000000, 0x0000000365000000| Untracked 
|  78|0x0000000366000000, 0x0000000367000000, 0x0000000367000000|100%| O|  |TAMS 0x0000000367000000, 0x0000000366000000| Untracked 
|  79|0x0000000367000000, 0x0000000368000000, 0x0000000368000000|100%| O|  |TAMS 0x0000000368000000, 0x0000000367000000| Untracked 
|  80|0x0000000368000000, 0x0000000369000000, 0x0000000369000000|100%| O|  |TAMS 0x0000000369000000, 0x0000000368000000| Untracked 
|  81|0x0000000369000000, 0x000000036a000000, 0x000000036a000000|100%| O|  |TAMS 0x000000036a000000, 0x0000000369000000| Untracked 
|  82|0x000000036a000000, 0x000000036b000000, 0x000000036b000000|100%| O|  |TAMS 0x000000036b000000, 0x000000036a000000| Untracked 
|  83|0x000000036b000000, 0x000000036c000000, 0x000000036c000000|100%| O|  |TAMS 0x000000036c000000, 0x000000036b000000| Untracked 
|  84|0x000000036c000000, 0x000000036d000000, 0x000000036d000000|100%| O|  |TAMS 0x000000036d000000, 0x000000036c000000| Untracked 
|  85|0x000000036d000000, 0x000000036e000000, 0x000000036e000000|100%| O|  |TAMS 0x000000036e000000, 0x000000036d000000| Untracked 
|  86|0x000000036e000000, 0x000000036f000000, 0x000000036f000000|100%| O|  |TAMS 0x000000036f000000, 0x000000036e000000| Untracked 
|  87|0x000000036f000000, 0x0000000370000000, 0x0000000370000000|100%| O|  |TAMS 0x0000000370000000, 0x000000036f000000| Untracked 
|  88|0x0000000370000000, 0x0000000371000000, 0x0000000371000000|100%| O|  |TAMS 0x0000000371000000, 0x0000000370000000| Untracked 
|  89|0x0000000371000000, 0x0000000372000000, 0x0000000372000000|100%| O|  |TAMS 0x0000000372000000, 0x0000000371000000| Untracked 
|  90|0x0000000372000000, 0x0000000373000000, 0x0000000373000000|100%| O|  |TAMS 0x0000000373000000, 0x0000000372000000| Untracked 
|  91|0x0000000373000000, 0x0000000374000000, 0x0000000374000000|100%| O|  |TAMS 0x0000000374000000, 0x0000000373000000| Untracked 
|  92|0x0000000374000000, 0x0000000375000000, 0x0000000375000000|100%| O|  |TAMS 0x0000000375000000, 0x0000000374000000| Untracked 
|  93|0x0000000375000000, 0x0000000376000000, 0x0000000376000000|100%| O|  |TAMS 0x0000000376000000, 0x0000000375000000| Untracked 
|  94|0x0000000376000000, 0x0000000377000000, 0x0000000377000000|100%| O|  |TAMS 0x0000000377000000, 0x0000000376000000| Untracked 
|  95|0x0000000377000000, 0x0000000378000000, 0x0000000378000000|100%| O|  |TAMS 0x0000000378000000, 0x0000000377000000| Untracked 
|  96|0x0000000378000000, 0x0000000379000000, 0x0000000379000000|100%| O|  |TAMS 0x0000000379000000, 0x0000000378000000| Untracked 
|  97|0x0000000379000000, 0x000000037a000000, 0x000000037a000000|100%| O|  |TAMS 0x000000037a000000, 0x0000000379000000| Untracked 
|  98|0x000000037a000000, 0x000000037b000000, 0x000000037b000000|100%| O|  |TAMS 0x000000037b000000, 0x000000037a000000| Untracked 
|  99|0x000000037b000000, 0x000000037c000000, 0x000000037c000000|100%| O|  |TAMS 0x000000037c000000, 0x000000037b000000| Untracked 
| 100|0x000000037c000000, 0x000000037d000000, 0x000000037d000000|100%| O|  |TAMS 0x000000037d000000, 0x000000037c000000| Untracked 
| 101|0x000000037d000000, 0x000000037e000000, 0x000000037e000000|100%| O|  |TAMS 0x000000037e000000, 0x000000037d000000| Untracked 
| 102|0x000000037e000000, 0x000000037f000000, 0x000000037f000000|100%| O|  |TAMS 0x000000037f000000, 0x000000037e000000| Untracked 
| 103|0x000000037f000000, 0x0000000380000000, 0x0000000380000000|100%| O|  |TAMS 0x0000000380000000, 0x000000037f000000| Untracked 
| 104|0x0000000380000000, 0x0000000381000000, 0x0000000381000000|100%| O|  |TAMS 0x0000000381000000, 0x0000000380000000| Untracked 
| 105|0x0000000381000000, 0x0000000382000000, 0x0000000382000000|100%| O|  |TAMS 0x0000000382000000, 0x0000000381000000| Untracked 
| 106|0x0000000382000000, 0x0000000383000000, 0x0000000383000000|100%| O|  |TAMS 0x0000000383000000, 0x0000000382000000| Untracked 
| 107|0x0000000383000000, 0x0000000384000000, 0x0000000384000000|100%| O|  |TAMS 0x0000000384000000, 0x0000000383000000| Untracked 
| 108|0x0000000384000000, 0x0000000385000000, 0x0000000385000000|100%| O|  |TAMS 0x0000000385000000, 0x0000000384000000| Untracked 
| 109|0x0000000385000000, 0x0000000386000000, 0x0000000386000000|100%| O|  |TAMS 0x0000000386000000, 0x0000000385000000| Untracked 
| 110|0x0000000386000000, 0x0000000387000000, 0x0000000387000000|100%| O|  |TAMS 0x0000000387000000, 0x0000000386000000| Untracked 
| 111|0x0000000387000000, 0x0000000388000000, 0x0000000388000000|100%| O|  |TAMS 0x0000000388000000, 0x0000000387000000| Untracked 
| 112|0x0000000388000000, 0x0000000389000000, 0x0000000389000000|100%| O|  |TAMS 0x0000000389000000, 0x0000000388000000| Untracked 
| 113|0x0000000389000000, 0x000000038a000000, 0x000000038a000000|100%| O|  |TAMS 0x000000038a000000, 0x0000000389000000| Untracked 
| 114|0x000000038a000000, 0x000000038b000000, 0x000000038b000000|100%| O|  |TAMS 0x000000038b000000, 0x000000038a000000| Untracked 
| 115|0x000000038b000000, 0x000000038c000000, 0x000000038c000000|100%| O|  |TAMS 0x000000038c000000, 0x000000038b000000| Untracked 
| 116|0x000000038c000000, 0x000000038d000000, 0x000000038d000000|100%| O|  |TAMS 0x000000038d000000, 0x000000038c000000| Untracked 
| 117|0x000000038d000000, 0x000000038e000000, 0x000000038e000000|100%| O|  |TAMS 0x000000038e000000, 0x000000038d000000| Untracked 
| 118|0x000000038e000000, 0x000000038f000000, 0x000000038f000000|100%| O|  |TAMS 0x000000038f000000, 0x000000038e000000| Untracked 
| 119|0x000000038f000000, 0x0000000390000000, 0x0000000390000000|100%| O|  |TAMS 0x000000038f000000, 0x000000038f000000| Untracked 
| 120|0x0000000390000000, 0x0000000391000000, 0x0000000391000000|100%| O|  |TAMS 0x0000000391000000, 0x0000000390000000| Untracked 
| 121|0x0000000391000000, 0x0000000392000000, 0x0000000392000000|100%| O|  |TAMS 0x0000000392000000, 0x0000000391000000| Untracked 
| 122|0x0000000392000000, 0x0000000393000000, 0x0000000393000000|100%| O|  |TAMS 0x0000000393000000, 0x0000000392000000| Untracked 
| 123|0x0000000393000000, 0x0000000394000000, 0x0000000394000000|100%| O|  |TAMS 0x0000000394000000, 0x0000000393000000| Untracked 
| 124|0x0000000394000000, 0x0000000395000000, 0x0000000395000000|100%| O|  |TAMS 0x0000000395000000, 0x0000000394000000| Untracked 
| 125|0x0000000395000000, 0x0000000396000000, 0x0000000396000000|100%| O|  |TAMS 0x0000000396000000, 0x0000000395000000| Untracked 
| 126|0x0000000396000000, 0x0000000397000000, 0x0000000397000000|100%| O|  |TAMS 0x0000000397000000, 0x0000000396000000| Untracked 
| 127|0x0000000397000000, 0x0000000398000000, 0x0000000398000000|100%| O|  |TAMS 0x0000000398000000, 0x0000000397000000| Untracked 
| 128|0x0000000398000000, 0x0000000399000000, 0x0000000399000000|100%| O|  |TAMS 0x0000000399000000, 0x0000000398000000| Untracked 
| 129|0x0000000399000000, 0x000000039a000000, 0x000000039a000000|100%| O|  |TAMS 0x000000039a000000, 0x0000000399000000| Untracked 
| 130|0x000000039a000000, 0x000000039b000000, 0x000000039b000000|100%| O|  |TAMS 0x000000039b000000, 0x000000039a000000| Untracked 
| 131|0x000000039b000000, 0x000000039c000000, 0x000000039c000000|100%| O|  |TAMS 0x000000039c000000, 0x000000039b000000| Untracked 
| 132|0x000000039c000000, 0x000000039d000000, 0x000000039d000000|100%| O|  |TAMS 0x000000039d000000, 0x000000039c000000| Untracked 
| 133|0x000000039d000000, 0x000000039e000000, 0x000000039e000000|100%| O|  |TAMS 0x000000039e000000, 0x000000039d000000| Untracked 
| 134|0x000000039e000000, 0x000000039f000000, 0x000000039f000000|100%| O|  |TAMS 0x000000039f000000, 0x000000039e000000| Untracked 
| 135|0x000000039f000000, 0x00000003a0000000, 0x00000003a0000000|100%| O|  |TAMS 0x00000003a0000000, 0x000000039f000000| Untracked 
| 136|0x00000003a0000000, 0x00000003a1000000, 0x00000003a1000000|100%| O|  |TAMS 0x00000003a1000000, 0x00000003a0000000| Untracked 
| 137|0x00000003a1000000, 0x00000003a2000000, 0x00000003a2000000|100%| O|  |TAMS 0x00000003a2000000, 0x00000003a1000000| Untracked 
| 138|0x00000003a2000000, 0x00000003a3000000, 0x00000003a3000000|100%| O|  |TAMS 0x00000003a3000000, 0x00000003a2000000| Untracked 
| 139|0x00000003a3000000, 0x00000003a4000000, 0x00000003a4000000|100%| O|  |TAMS 0x00000003a4000000, 0x00000003a3000000| Untracked 
| 140|0x00000003a4000000, 0x00000003a5000000, 0x00000003a5000000|100%| O|  |TAMS 0x00000003a5000000, 0x00000003a4000000| Untracked 
| 141|0x00000003a5000000, 0x00000003a6000000, 0x00000003a6000000|100%| O|  |TAMS 0x00000003a6000000, 0x00000003a5000000| Untracked 
| 142|0x00000003a6000000, 0x00000003a7000000, 0x00000003a7000000|100%| O|  |TAMS 0x00000003a7000000, 0x00000003a6000000| Untracked 
| 143|0x00000003a7000000, 0x00000003a8000000, 0x00000003a8000000|100%| O|  |TAMS 0x00000003a8000000, 0x00000003a7000000| Untracked 
| 144|0x00000003a8000000, 0x00000003a9000000, 0x00000003a9000000|100%| O|  |TAMS 0x00000003a9000000, 0x00000003a8000000| Untracked 
| 145|0x00000003a9000000, 0x00000003aa000000, 0x00000003aa000000|100%| O|  |TAMS 0x00000003aa000000, 0x00000003a9000000| Untracked 
| 146|0x00000003aa000000, 0x00000003ab000000, 0x00000003ab000000|100%|HS|  |TAMS 0x00000003ab000000, 0x00000003aa000000| Complete 
| 147|0x00000003ab000000, 0x00000003ac000000, 0x00000003ac000000|100%|HS|  |TAMS 0x00000003ac000000, 0x00000003ab000000| Complete 
| 148|0x00000003ac000000, 0x00000003ad000000, 0x00000003ad000000|100%|HS|  |TAMS 0x00000003ad000000, 0x00000003ac000000| Complete 
| 149|0x00000003ad000000, 0x00000003ae000000, 0x00000003ae000000|100%|HS|  |TAMS 0x00000003ae000000, 0x00000003ad000000| Complete 
| 150|0x00000003ae000000, 0x00000003af000000, 0x00000003af000000|100%| O|  |TAMS 0x00000003af000000, 0x00000003ae000000| Untracked 
| 151|0x00000003af000000, 0x00000003b0000000, 0x00000003b0000000|100%| O|  |TAMS 0x00000003b0000000, 0x00000003af000000| Untracked 
| 152|0x00000003b0000000, 0x00000003b1000000, 0x00000003b1000000|100%| O|  |TAMS 0x00000003b1000000, 0x00000003b0000000| Untracked 
| 153|0x00000003b1000000, 0x00000003b2000000, 0x00000003b2000000|100%| O|  |TAMS 0x00000003b2000000, 0x00000003b1000000| Untracked 
| 154|0x00000003b2000000, 0x00000003b3000000, 0x00000003b3000000|100%| O|  |TAMS 0x00000003b3000000, 0x00000003b2000000| Untracked 
| 155|0x00000003b3000000, 0x00000003b4000000, 0x00000003b4000000|100%| O|  |TAMS 0x00000003b4000000, 0x00000003b3000000| Untracked 
| 156|0x00000003b4000000, 0x00000003b5000000, 0x00000003b5000000|100%| O|  |TAMS 0x00000003b5000000, 0x00000003b4000000| Untracked 
| 157|0x00000003b5000000, 0x00000003b6000000, 0x00000003b6000000|100%| O|  |TAMS 0x00000003b6000000, 0x00000003b5000000| Untracked 
| 158|0x00000003b6000000, 0x00000003b7000000, 0x00000003b7000000|100%| O|  |TAMS 0x00000003b7000000, 0x00000003b6000000| Untracked 
| 159|0x00000003b7000000, 0x00000003b8000000, 0x00000003b8000000|100%| O|  |TAMS 0x00000003b8000000, 0x00000003b7000000| Untracked 
| 160|0x00000003b8000000, 0x00000003b9000000, 0x00000003b9000000|100%| O|  |TAMS 0x00000003b9000000, 0x00000003b8000000| Untracked 
| 161|0x00000003b9000000, 0x00000003ba000000, 0x00000003ba000000|100%| O|  |TAMS 0x00000003ba000000, 0x00000003b9000000| Untracked 
| 162|0x00000003ba000000, 0x00000003bb000000, 0x00000003bb000000|100%| O|  |TAMS 0x00000003bb000000, 0x00000003ba000000| Untracked 
| 163|0x00000003bb000000, 0x00000003bc000000, 0x00000003bc000000|100%| O|  |TAMS 0x00000003bc000000, 0x00000003bb000000| Untracked 
| 164|0x00000003bc000000, 0x00000003bd000000, 0x00000003bd000000|100%| O|  |TAMS 0x00000003bd000000, 0x00000003bc000000| Untracked 
| 165|0x00000003bd000000, 0x00000003be000000, 0x00000003be000000|100%| O|  |TAMS 0x00000003be000000, 0x00000003bd000000| Untracked 
| 166|0x00000003be000000, 0x00000003bf000000, 0x00000003bf000000|100%| O|  |TAMS 0x00000003bf000000, 0x00000003be000000| Untracked 
| 167|0x00000003bf000000, 0x00000003c0000000, 0x00000003c0000000|100%| O|  |TAMS 0x00000003c0000000, 0x00000003bf000000| Untracked 
| 168|0x00000003c0000000, 0x00000003c1000000, 0x00000003c1000000|100%| O|  |TAMS 0x00000003c1000000, 0x00000003c0000000| Untracked 
| 169|0x00000003c1000000, 0x00000003c2000000, 0x00000003c2000000|100%| O|  |TAMS 0x00000003c2000000, 0x00000003c1000000| Untracked 
| 170|0x00000003c2000000, 0x00000003c3000000, 0x00000003c3000000|100%| O|  |TAMS 0x00000003c3000000, 0x00000003c2000000| Untracked 
| 171|0x00000003c3000000, 0x00000003c4000000, 0x00000003c4000000|100%| O|  |TAMS 0x00000003c4000000, 0x00000003c3000000| Untracked 
| 172|0x00000003c4000000, 0x00000003c5000000, 0x00000003c5000000|100%| O|  |TAMS 0x00000003c5000000, 0x00000003c4000000| Untracked 
| 173|0x00000003c5000000, 0x00000003c6000000, 0x00000003c6000000|100%| O|  |TAMS 0x00000003c6000000, 0x00000003c5000000| Untracked 
| 174|0x00000003c6000000, 0x00000003c7000000, 0x00000003c7000000|100%| O|  |TAMS 0x00000003c7000000, 0x00000003c6000000| Untracked 
| 175|0x00000003c7000000, 0x00000003c8000000, 0x00000003c8000000|100%| O|  |TAMS 0x00000003c8000000, 0x00000003c7000000| Untracked 
| 176|0x00000003c8000000, 0x00000003c9000000, 0x00000003c9000000|100%| O|  |TAMS 0x00000003c9000000, 0x00000003c8000000| Untracked 
| 177|0x00000003c9000000, 0x00000003ca000000, 0x00000003ca000000|100%| O|  |TAMS 0x00000003ca000000, 0x00000003c9000000| Untracked 
| 178|0x00000003ca000000, 0x00000003cb000000, 0x00000003cb000000|100%| O|  |TAMS 0x00000003cb000000, 0x00000003ca000000| Untracked 
| 179|0x00000003cb000000, 0x00000003cc000000, 0x00000003cc000000|100%| O|  |TAMS 0x00000003cc000000, 0x00000003cb000000| Untracked 
| 180|0x00000003cc000000, 0x00000003cd000000, 0x00000003cd000000|100%| O|  |TAMS 0x00000003cd000000, 0x00000003cc000000| Untracked 
| 181|0x00000003cd000000, 0x00000003ce000000, 0x00000003ce000000|100%| O|  |TAMS 0x00000003cd000000, 0x00000003cd000000| Untracked 
| 182|0x00000003ce000000, 0x00000003cf000000, 0x00000003cf000000|100%| O|  |TAMS 0x00000003cf000000, 0x00000003ce000000| Untracked 
| 183|0x00000003cf000000, 0x00000003d0000000, 0x00000003d0000000|100%| O|  |TAMS 0x00000003d0000000, 0x00000003cf000000| Untracked 
| 184|0x00000003d0000000, 0x00000003d1000000, 0x00000003d1000000|100%| O|  |TAMS 0x00000003d1000000, 0x00000003d0000000| Untracked 
| 185|0x00000003d1000000, 0x00000003d2000000, 0x00000003d2000000|100%| O|  |TAMS 0x00000003d2000000, 0x00000003d1000000| Untracked 
| 186|0x00000003d2000000, 0x00000003d3000000, 0x00000003d3000000|100%| O|  |TAMS 0x00000003d3000000, 0x00000003d2000000| Untracked 
| 187|0x00000003d3000000, 0x00000003d4000000, 0x00000003d4000000|100%| O|  |TAMS 0x00000003d4000000, 0x00000003d3000000| Untracked 
| 188|0x00000003d4000000, 0x00000003d5000000, 0x00000003d5000000|100%| O|  |TAMS 0x00000003d5000000, 0x00000003d4000000| Untracked 
| 189|0x00000003d5000000, 0x00000003d6000000, 0x00000003d6000000|100%| O|  |TAMS 0x00000003d6000000, 0x00000003d5000000| Untracked 
| 190|0x00000003d6000000, 0x00000003d7000000, 0x00000003d7000000|100%| O|  |TAMS 0x00000003d7000000, 0x00000003d6000000| Untracked 
| 191|0x00000003d7000000, 0x00000003d8000000, 0x00000003d8000000|100%| O|  |TAMS 0x00000003d8000000, 0x00000003d7000000| Untracked 
| 192|0x00000003d8000000, 0x00000003d9000000, 0x00000003d9000000|100%| O|  |TAMS 0x00000003d9000000, 0x00000003d8000000| Untracked 
| 193|0x00000003d9000000, 0x00000003da000000, 0x00000003da000000|100%| O|  |TAMS 0x00000003da000000, 0x00000003d9000000| Untracked 
| 194|0x00000003da000000, 0x00000003db000000, 0x00000003db000000|100%| O|  |TAMS 0x00000003db000000, 0x00000003da000000| Untracked 
| 195|0x00000003db000000, 0x00000003dc000000, 0x00000003dc000000|100%| O|  |TAMS 0x00000003dc000000, 0x00000003db000000| Untracked 
| 196|0x00000003dc000000, 0x00000003dd000000, 0x00000003dd000000|100%| O|  |TAMS 0x00000003dd000000, 0x00000003dc000000| Untracked 
| 197|0x00000003dd000000, 0x00000003de000000, 0x00000003de000000|100%| O|  |TAMS 0x00000003de000000, 0x00000003dd000000| Untracked 
| 198|0x00000003de000000, 0x00000003df000000, 0x00000003df000000|100%| O|  |TAMS 0x00000003df000000, 0x00000003de000000| Untracked 
| 199|0x00000003df000000, 0x00000003e0000000, 0x00000003e0000000|100%| O|  |TAMS 0x00000003e0000000, 0x00000003df000000| Untracked 
| 200|0x00000003e0000000, 0x00000003e1000000, 0x00000003e1000000|100%| O|  |TAMS 0x00000003e1000000, 0x00000003e0000000| Untracked 
| 201|0x00000003e1000000, 0x00000003e2000000, 0x00000003e2000000|100%| O|  |TAMS 0x00000003e1000000, 0x00000003e1000000| Untracked 
| 202|0x00000003e2000000, 0x00000003e3000000, 0x00000003e3000000|100%| O|  |TAMS 0x00000003e2000000, 0x00000003e2000000| Untracked 
| 203|0x00000003e3000000, 0x00000003e4000000, 0x00000003e4000000|100%| O|  |TAMS 0x00000003e3000000, 0x00000003e3000000| Untracked 
| 204|0x00000003e4000000, 0x00000003e5000000, 0x00000003e5000000|100%| O|  |TAMS 0x00000003e5000000, 0x00000003e4000000| Untracked 
| 205|0x00000003e5000000, 0x00000003e6000000, 0x00000003e6000000|100%| O|  |TAMS 0x00000003e5000000, 0x00000003e5000000| Untracked 
| 206|0x00000003e6000000, 0x00000003e7000000, 0x00000003e7000000|100%|HS|  |TAMS 0x00000003e7000000, 0x00000003e6000000| Complete 
| 207|0x00000003e7000000, 0x00000003e8000000, 0x00000003e8000000|100%| O|  |TAMS 0x00000003e8000000, 0x00000003e7000000| Untracked 
| 208|0x00000003e8000000, 0x00000003e9000000, 0x00000003e9000000|100%| O|  |TAMS 0x00000003e9000000, 0x00000003e8000000| Untracked 
| 209|0x00000003e9000000, 0x00000003ea000000, 0x00000003ea000000|100%| O|  |TAMS 0x00000003ea000000, 0x00000003e9000000| Untracked 
| 210|0x00000003ea000000, 0x00000003eb000000, 0x00000003eb000000|100%| O|  |TAMS 0x00000003eb000000, 0x00000003ea000000| Untracked 
| 211|0x00000003eb000000, 0x00000003ec000000, 0x00000003ec000000|100%| O|  |TAMS 0x00000003ec000000, 0x00000003eb000000| Untracked 
| 212|0x00000003ec000000, 0x00000003ed000000, 0x00000003ed000000|100%| O|  |TAMS 0x00000003ed000000, 0x00000003ec000000| Untracked 
| 213|0x00000003ed000000, 0x00000003ee000000, 0x00000003ee000000|100%| O|  |TAMS 0x00000003ee000000, 0x00000003ed000000| Untracked 
| 214|0x00000003ee000000, 0x00000003ef000000, 0x00000003ef000000|100%| O|  |TAMS 0x00000003ef000000, 0x00000003ee000000| Untracked 
| 215|0x00000003ef000000, 0x00000003f0000000, 0x00000003f0000000|100%| O|  |TAMS 0x00000003f0000000, 0x00000003ef000000| Untracked 
| 216|0x00000003f0000000, 0x00000003f1000000, 0x00000003f1000000|100%| O|  |TAMS 0x00000003f1000000, 0x00000003f0000000| Untracked 
| 217|0x00000003f1000000, 0x00000003f2000000, 0x00000003f2000000|100%| O|  |TAMS 0x00000003f2000000, 0x00000003f1000000| Untracked 
| 218|0x00000003f2000000, 0x00000003f3000000, 0x00000003f3000000|100%| O|  |TAMS 0x00000003f3000000, 0x00000003f2000000| Untracked 
| 219|0x00000003f3000000, 0x00000003f4000000, 0x00000003f4000000|100%| O|  |TAMS 0x00000003f4000000, 0x00000003f3000000| Untracked 
| 220|0x00000003f4000000, 0x00000003f5000000, 0x00000003f5000000|100%| O|  |TAMS 0x00000003f5000000, 0x00000003f4000000| Untracked 
| 221|0x00000003f5000000, 0x00000003f6000000, 0x00000003f6000000|100%| O|  |TAMS 0x00000003f6000000, 0x00000003f5000000| Untracked 
| 222|0x00000003f6000000, 0x00000003f7000000, 0x00000003f7000000|100%| O|  |TAMS 0x00000003f7000000, 0x00000003f6000000| Untracked 
| 223|0x00000003f7000000, 0x00000003f8000000, 0x00000003f8000000|100%| O|  |TAMS 0x00000003f8000000, 0x00000003f7000000| Untracked 
| 224|0x00000003f8000000, 0x00000003f9000000, 0x00000003f9000000|100%|HS|  |TAMS 0x00000003f9000000, 0x00000003f8000000| Complete 
| 225|0x00000003f9000000, 0x00000003fa000000, 0x00000003fa000000|100%|HC|  |TAMS 0x00000003fa000000, 0x00000003f9000000| Complete 
| 226|0x00000003fa000000, 0x00000003fb000000, 0x00000003fb000000|100%| O|  |TAMS 0x00000003fb000000, 0x00000003fa000000| Untracked 
| 227|0x00000003fb000000, 0x00000003fc000000, 0x00000003fc000000|100%| O|  |TAMS 0x00000003fc000000, 0x00000003fb000000| Untracked 
| 228|0x00000003fc000000, 0x00000003fd000000, 0x00000003fd000000|100%| O|  |TAMS 0x00000003fd000000, 0x00000003fc000000| Untracked 
| 229|0x00000003fd000000, 0x00000003fe000000, 0x00000003fe000000|100%| O|  |TAMS 0x00000003fe000000, 0x00000003fd000000| Untracked 
| 230|0x00000003fe000000, 0x00000003ff000000, 0x00000003ff000000|100%| O|  |TAMS 0x00000003ff000000, 0x00000003fe000000| Untracked 
| 231|0x00000003ff000000, 0x0000000400000000, 0x0000000400000000|100%| O|  |TAMS 0x0000000400000000, 0x00000003ff000000| Untracked 
| 232|0x0000000400000000, 0x0000000401000000, 0x0000000401000000|100%| O|  |TAMS 0x0000000401000000, 0x0000000400000000| Untracked 
| 233|0x0000000401000000, 0x0000000402000000, 0x0000000402000000|100%| O|  |TAMS 0x0000000402000000, 0x0000000401000000| Untracked 
| 234|0x0000000402000000, 0x0000000403000000, 0x0000000403000000|100%| O|  |TAMS 0x0000000403000000, 0x0000000402000000| Untracked 
| 235|0x0000000403000000, 0x0000000404000000, 0x0000000404000000|100%| O|  |TAMS 0x0000000404000000, 0x0000000403000000| Untracked 
| 236|0x0000000404000000, 0x0000000405000000, 0x0000000405000000|100%| O|  |TAMS 0x0000000405000000, 0x0000000404000000| Untracked 
| 237|0x0000000405000000, 0x0000000406000000, 0x0000000406000000|100%| O|  |TAMS 0x0000000406000000, 0x0000000405000000| Untracked 
| 238|0x0000000406000000, 0x0000000407000000, 0x0000000407000000|100%| O|  |TAMS 0x0000000407000000, 0x0000000406000000| Untracked 
| 239|0x0000000407000000, 0x0000000408000000, 0x0000000408000000|100%| O|  |TAMS 0x0000000407000000, 0x0000000407000000| Untracked 
| 240|0x0000000408000000, 0x0000000409000000, 0x0000000409000000|100%|HS|  |TAMS 0x0000000409000000, 0x0000000408000000| Complete 
| 241|0x0000000409000000, 0x000000040a000000, 0x000000040a000000|100%|HC|  |TAMS 0x000000040a000000, 0x0000000409000000| Complete 
| 242|0x000000040a000000, 0x000000040b000000, 0x000000040b000000|100%|HS|  |TAMS 0x000000040b000000, 0x000000040a000000| Complete 
| 243|0x000000040b000000, 0x000000040c000000, 0x000000040c000000|100%|HS|  |TAMS 0x000000040c000000, 0x000000040b000000| Complete 
| 244|0x000000040c000000, 0x000000040d000000, 0x000000040d000000|100%| O|  |TAMS 0x000000040d000000, 0x000000040c000000| Untracked 
| 245|0x000000040d000000, 0x000000040e000000, 0x000000040e000000|100%| O|  |TAMS 0x000000040e000000, 0x000000040d000000| Untracked 
| 246|0x000000040e000000, 0x000000040f000000, 0x000000040f000000|100%| O|  |TAMS 0x000000040f000000, 0x000000040e000000| Untracked 
| 247|0x000000040f000000, 0x0000000410000000, 0x0000000410000000|100%| O|  |TAMS 0x0000000410000000, 0x000000040f000000| Untracked 
| 248|0x0000000410000000, 0x0000000411000000, 0x0000000411000000|100%| O|  |TAMS 0x0000000411000000, 0x0000000410000000| Untracked 
| 249|0x0000000411000000, 0x0000000412000000, 0x0000000412000000|100%| O|  |TAMS 0x0000000412000000, 0x0000000411000000| Untracked 
| 250|0x0000000412000000, 0x0000000413000000, 0x0000000413000000|100%| O|  |TAMS 0x0000000413000000, 0x0000000412000000| Untracked 
| 251|0x0000000413000000, 0x0000000414000000, 0x0000000414000000|100%| O|  |TAMS 0x0000000414000000, 0x0000000413000000| Untracked 
| 252|0x0000000414000000, 0x0000000415000000, 0x0000000415000000|100%| O|  |TAMS 0x0000000415000000, 0x0000000414000000| Untracked 
| 253|0x0000000415000000, 0x0000000416000000, 0x0000000416000000|100%| O|  |TAMS 0x0000000416000000, 0x0000000415000000| Untracked 
| 254|0x0000000416000000, 0x0000000417000000, 0x0000000417000000|100%| O|  |TAMS 0x0000000417000000, 0x0000000416000000| Untracked 
| 255|0x0000000417000000, 0x0000000418000000, 0x0000000418000000|100%| O|  |TAMS 0x0000000418000000, 0x0000000417000000| Untracked 
| 256|0x0000000418000000, 0x0000000419000000, 0x0000000419000000|100%| O|  |TAMS 0x0000000419000000, 0x0000000418000000| Untracked 
| 257|0x0000000419000000, 0x000000041a000000, 0x000000041a000000|100%| O|  |TAMS 0x000000041a000000, 0x0000000419000000| Untracked 
| 258|0x000000041a000000, 0x000000041b000000, 0x000000041b000000|100%| O|  |TAMS 0x000000041b000000, 0x000000041a000000| Untracked 
| 259|0x000000041b000000, 0x000000041c000000, 0x000000041c000000|100%| O|  |TAMS 0x000000041c000000, 0x000000041b000000| Untracked 
| 260|0x000000041c000000, 0x000000041d000000, 0x000000041d000000|100%| O|  |TAMS 0x000000041d000000, 0x000000041c000000| Untracked 
| 261|0x000000041d000000, 0x000000041e000000, 0x000000041e000000|100%| O|  |TAMS 0x000000041e000000, 0x000000041d000000| Untracked 
| 262|0x000000041e000000, 0x000000041f000000, 0x000000041f000000|100%| O|  |TAMS 0x000000041f000000, 0x000000041e000000| Untracked 
| 263|0x000000041f000000, 0x0000000420000000, 0x0000000420000000|100%| O|  |TAMS 0x0000000420000000, 0x000000041f000000| Untracked 
| 264|0x0000000420000000, 0x0000000421000000, 0x0000000421000000|100%| O|  |TAMS 0x0000000421000000, 0x0000000420000000| Untracked 
| 265|0x0000000421000000, 0x0000000422000000, 0x0000000422000000|100%| O|  |TAMS 0x0000000422000000, 0x0000000421000000| Untracked 
| 266|0x0000000422000000, 0x0000000423000000, 0x0000000423000000|100%| O|  |TAMS 0x0000000423000000, 0x0000000422000000| Untracked 
| 267|0x0000000423000000, 0x0000000424000000, 0x0000000424000000|100%| O|  |TAMS 0x0000000424000000, 0x0000000423000000| Untracked 
| 268|0x0000000424000000, 0x0000000425000000, 0x0000000425000000|100%| O|  |TAMS 0x0000000425000000, 0x0000000424000000| Untracked 
| 269|0x0000000425000000, 0x0000000426000000, 0x0000000426000000|100%| O|  |TAMS 0x0000000426000000, 0x0000000425000000| Untracked 
| 270|0x0000000426000000, 0x0000000427000000, 0x0000000427000000|100%| O|  |TAMS 0x0000000427000000, 0x0000000426000000| Untracked 
| 271|0x0000000427000000, 0x0000000428000000, 0x0000000428000000|100%| O|  |TAMS 0x0000000428000000, 0x0000000427000000| Untracked 
| 272|0x0000000428000000, 0x0000000429000000, 0x0000000429000000|100%| O|  |TAMS 0x0000000429000000, 0x0000000428000000| Untracked 
| 273|0x0000000429000000, 0x000000042a000000, 0x000000042a000000|100%| O|  |TAMS 0x000000042a000000, 0x0000000429000000| Untracked 
| 274|0x000000042a000000, 0x000000042b000000, 0x000000042b000000|100%| O|  |TAMS 0x000000042b000000, 0x000000042a000000| Untracked 
| 275|0x000000042b000000, 0x000000042c000000, 0x000000042c000000|100%| O|  |TAMS 0x000000042c000000, 0x000000042b000000| Untracked 
| 276|0x000000042c000000, 0x000000042d000000, 0x000000042d000000|100%| O|  |TAMS 0x000000042d000000, 0x000000042c000000| Untracked 
| 277|0x000000042d000000, 0x000000042e000000, 0x000000042e000000|100%| O|  |TAMS 0x000000042e000000, 0x000000042d000000| Untracked 
| 278|0x000000042e000000, 0x000000042f000000, 0x000000042f000000|100%| O|  |TAMS 0x000000042f000000, 0x000000042e000000| Untracked 
| 279|0x000000042f000000, 0x0000000430000000, 0x0000000430000000|100%| O|  |TAMS 0x0000000430000000, 0x000000042f000000| Untracked 
| 280|0x0000000430000000, 0x0000000431000000, 0x0000000431000000|100%| O|  |TAMS 0x0000000431000000, 0x0000000430000000| Untracked 
| 281|0x0000000431000000, 0x0000000432000000, 0x0000000432000000|100%| O|  |TAMS 0x0000000432000000, 0x0000000431000000| Untracked 
| 282|0x0000000432000000, 0x0000000433000000, 0x0000000433000000|100%| O|  |TAMS 0x0000000433000000, 0x0000000432000000| Untracked 
| 283|0x0000000433000000, 0x0000000434000000, 0x0000000434000000|100%| O|  |TAMS 0x0000000434000000, 0x0000000433000000| Untracked 
| 284|0x0000000434000000, 0x0000000435000000, 0x0000000435000000|100%| O|  |TAMS 0x0000000435000000, 0x0000000434000000| Untracked 
| 285|0x0000000435000000, 0x0000000436000000, 0x0000000436000000|100%| O|  |TAMS 0x0000000436000000, 0x0000000435000000| Untracked 
| 286|0x0000000436000000, 0x0000000437000000, 0x0000000437000000|100%| O|  |TAMS 0x0000000437000000, 0x0000000436000000| Untracked 
| 287|0x0000000437000000, 0x0000000438000000, 0x0000000438000000|100%| O|  |TAMS 0x0000000438000000, 0x0000000437000000| Untracked 
| 288|0x0000000438000000, 0x0000000439000000, 0x0000000439000000|100%| O|  |TAMS 0x0000000439000000, 0x0000000438000000| Untracked 
| 289|0x0000000439000000, 0x000000043a000000, 0x000000043a000000|100%| O|  |TAMS 0x000000043a000000, 0x0000000439000000| Untracked 
| 290|0x000000043a000000, 0x000000043b000000, 0x000000043b000000|100%| O|  |TAMS 0x000000043b000000, 0x000000043a000000| Untracked 
| 291|0x000000043b000000, 0x000000043c000000, 0x000000043c000000|100%| O|  |TAMS 0x000000043c000000, 0x000000043b000000| Untracked 
| 292|0x000000043c000000, 0x000000043d000000, 0x000000043d000000|100%| O|  |TAMS 0x000000043d000000, 0x000000043c000000| Untracked 
| 293|0x000000043d000000, 0x000000043e000000, 0x000000043e000000|100%| O|  |TAMS 0x000000043e000000, 0x000000043d000000| Untracked 
| 294|0x000000043e000000, 0x000000043f000000, 0x000000043f000000|100%| O|  |TAMS 0x000000043f000000, 0x000000043e000000| Untracked 
| 295|0x000000043f000000, 0x0000000440000000, 0x0000000440000000|100%| O|  |TAMS 0x0000000440000000, 0x000000043f000000| Untracked 
| 296|0x0000000440000000, 0x0000000441000000, 0x0000000441000000|100%| O|  |TAMS 0x0000000441000000, 0x0000000440000000| Untracked 
| 297|0x0000000441000000, 0x0000000442000000, 0x0000000442000000|100%| O|  |TAMS 0x0000000442000000, 0x0000000441000000| Untracked 
| 298|0x0000000442000000, 0x0000000443000000, 0x0000000443000000|100%| O|  |TAMS 0x0000000443000000, 0x0000000442000000| Untracked 
| 299|0x0000000443000000, 0x0000000444000000, 0x0000000444000000|100%| O|  |TAMS 0x0000000444000000, 0x0000000443000000| Untracked 
| 300|0x0000000444000000, 0x0000000445000000, 0x0000000445000000|100%| O|  |TAMS 0x0000000445000000, 0x0000000444000000| Untracked 
| 301|0x0000000445000000, 0x0000000446000000, 0x0000000446000000|100%| O|  |TAMS 0x0000000446000000, 0x0000000445000000| Untracked 
| 302|0x0000000446000000, 0x0000000447000000, 0x0000000447000000|100%| O|  |TAMS 0x0000000447000000, 0x0000000446000000| Untracked 
| 303|0x0000000447000000, 0x0000000448000000, 0x0000000448000000|100%| O|  |TAMS 0x0000000448000000, 0x0000000447000000| Untracked 
| 304|0x0000000448000000, 0x0000000449000000, 0x0000000449000000|100%| O|  |TAMS 0x0000000449000000, 0x0000000448000000| Untracked 
| 305|0x0000000449000000, 0x000000044a000000, 0x000000044a000000|100%| O|  |TAMS 0x000000044a000000, 0x0000000449000000| Untracked 
| 306|0x000000044a000000, 0x000000044b000000, 0x000000044b000000|100%| O|  |TAMS 0x000000044b000000, 0x000000044a000000| Untracked 
| 307|0x000000044b000000, 0x000000044c000000, 0x000000044c000000|100%| O|  |TAMS 0x000000044c000000, 0x000000044b000000| Untracked 
| 308|0x000000044c000000, 0x000000044d000000, 0x000000044d000000|100%| O|  |TAMS 0x000000044d000000, 0x000000044c000000| Untracked 
| 309|0x000000044d000000, 0x000000044e000000, 0x000000044e000000|100%| O|  |TAMS 0x000000044e000000, 0x000000044d000000| Untracked 
| 310|0x000000044e000000, 0x000000044f000000, 0x000000044f000000|100%| O|  |TAMS 0x000000044f000000, 0x000000044e000000| Untracked 
| 311|0x000000044f000000, 0x0000000450000000, 0x0000000450000000|100%| O|  |TAMS 0x0000000450000000, 0x000000044f000000| Untracked 
| 312|0x0000000450000000, 0x0000000451000000, 0x0000000451000000|100%| O|  |TAMS 0x0000000451000000, 0x0000000450000000| Untracked 
| 313|0x0000000451000000, 0x0000000452000000, 0x0000000452000000|100%| O|  |TAMS 0x0000000452000000, 0x0000000451000000| Untracked 
| 314|0x0000000452000000, 0x0000000453000000, 0x0000000453000000|100%| O|  |TAMS 0x0000000453000000, 0x0000000452000000| Untracked 
| 315|0x0000000453000000, 0x0000000454000000, 0x0000000454000000|100%| O|  |TAMS 0x0000000454000000, 0x0000000453000000| Untracked 
| 316|0x0000000454000000, 0x0000000455000000, 0x0000000455000000|100%| O|  |TAMS 0x0000000455000000, 0x0000000454000000| Untracked 
| 317|0x0000000455000000, 0x0000000456000000, 0x0000000456000000|100%| O|  |TAMS 0x0000000456000000, 0x0000000455000000| Untracked 
| 318|0x0000000456000000, 0x0000000457000000, 0x0000000457000000|100%| O|  |TAMS 0x0000000457000000, 0x0000000456000000| Untracked 
| 319|0x0000000457000000, 0x0000000458000000, 0x0000000458000000|100%| O|  |TAMS 0x0000000458000000, 0x0000000457000000| Untracked 
| 320|0x0000000458000000, 0x0000000459000000, 0x0000000459000000|100%| O|  |TAMS 0x0000000459000000, 0x0000000458000000| Untracked 
| 321|0x0000000459000000, 0x000000045a000000, 0x000000045a000000|100%| O|  |TAMS 0x000000045a000000, 0x0000000459000000| Untracked 
| 322|0x000000045a000000, 0x000000045b000000, 0x000000045b000000|100%| O|  |TAMS 0x000000045b000000, 0x000000045a000000| Untracked 
| 323|0x000000045b000000, 0x000000045c000000, 0x000000045c000000|100%| O|  |TAMS 0x000000045c000000, 0x000000045b000000| Untracked 
| 324|0x000000045c000000, 0x000000045d000000, 0x000000045d000000|100%| O|  |TAMS 0x000000045d000000, 0x000000045c000000| Untracked 
| 325|0x000000045d000000, 0x000000045e000000, 0x000000045e000000|100%| O|  |TAMS 0x000000045e000000, 0x000000045d000000| Untracked 
| 326|0x000000045e000000, 0x000000045f000000, 0x000000045f000000|100%| O|  |TAMS 0x000000045f000000, 0x000000045e000000| Untracked 
| 327|0x000000045f000000, 0x0000000460000000, 0x0000000460000000|100%| O|  |TAMS 0x0000000460000000, 0x000000045f000000| Untracked 
| 328|0x0000000460000000, 0x0000000461000000, 0x0000000461000000|100%| O|  |TAMS 0x0000000461000000, 0x0000000460000000| Untracked 
| 329|0x0000000461000000, 0x0000000462000000, 0x0000000462000000|100%| O|  |TAMS 0x0000000462000000, 0x0000000461000000| Untracked 
| 330|0x0000000462000000, 0x0000000463000000, 0x0000000463000000|100%| O|  |TAMS 0x0000000463000000, 0x0000000462000000| Untracked 
| 331|0x0000000463000000, 0x0000000464000000, 0x0000000464000000|100%| O|  |TAMS 0x0000000464000000, 0x0000000463000000| Untracked 
| 332|0x0000000464000000, 0x0000000465000000, 0x0000000465000000|100%| O|  |TAMS 0x0000000465000000, 0x0000000464000000| Untracked 
| 333|0x0000000465000000, 0x0000000466000000, 0x0000000466000000|100%| O|  |TAMS 0x0000000466000000, 0x0000000465000000| Untracked 
| 334|0x0000000466000000, 0x0000000467000000, 0x0000000467000000|100%| O|  |TAMS 0x0000000467000000, 0x0000000466000000| Untracked 
| 335|0x0000000467000000, 0x0000000468000000, 0x0000000468000000|100%| O|  |TAMS 0x0000000467000000, 0x0000000467000000| Untracked 
| 336|0x0000000468000000, 0x0000000469000000, 0x0000000469000000|100%| O|  |TAMS 0x0000000468000000, 0x0000000468000000| Untracked 
| 337|0x0000000469000000, 0x000000046a000000, 0x000000046a000000|100%| O|  |TAMS 0x000000046a000000, 0x0000000469000000| Untracked 
| 338|0x000000046a000000, 0x000000046b000000, 0x000000046b000000|100%| O|  |TAMS 0x000000046a000000, 0x000000046a000000| Untracked 
| 339|0x000000046b000000, 0x000000046c000000, 0x000000046c000000|100%| O|  |TAMS 0x000000046c000000, 0x000000046b000000| Untracked 
| 340|0x000000046c000000, 0x000000046d000000, 0x000000046d000000|100%| O|  |TAMS 0x000000046d000000, 0x000000046c000000| Untracked 
| 341|0x000000046d000000, 0x000000046e000000, 0x000000046e000000|100%| O|  |TAMS 0x000000046e000000, 0x000000046d000000| Untracked 
| 342|0x000000046e000000, 0x000000046f000000, 0x000000046f000000|100%| O|  |TAMS 0x000000046e000000, 0x000000046e000000| Untracked 
| 343|0x000000046f000000, 0x0000000470000000, 0x0000000470000000|100%| O|  |TAMS 0x000000046f000000, 0x000000046f000000| Untracked 
| 344|0x0000000470000000, 0x0000000471000000, 0x0000000471000000|100%| O|  |TAMS 0x0000000470000000, 0x0000000470000000| Untracked 
| 345|0x0000000471000000, 0x0000000472000000, 0x0000000472000000|100%| O|  |TAMS 0x0000000471000000, 0x0000000471000000| Untracked 
| 346|0x0000000472000000, 0x0000000473000000, 0x0000000473000000|100%| O|  |TAMS 0x0000000473000000, 0x0000000472000000| Untracked 
| 347|0x0000000473000000, 0x0000000474000000, 0x0000000474000000|100%| O|  |TAMS 0x0000000474000000, 0x0000000473000000| Untracked 
| 348|0x0000000474000000, 0x0000000475000000, 0x0000000475000000|100%| O|  |TAMS 0x0000000475000000, 0x0000000474000000| Untracked 
| 349|0x0000000475000000, 0x0000000476000000, 0x0000000476000000|100%| O|  |TAMS 0x0000000476000000, 0x0000000475000000| Untracked 
| 350|0x0000000476000000, 0x0000000477000000, 0x0000000477000000|100%| O|  |TAMS 0x0000000477000000, 0x0000000476000000| Untracked 
| 351|0x0000000477000000, 0x0000000478000000, 0x0000000478000000|100%| O|  |TAMS 0x0000000478000000, 0x0000000477000000| Untracked 
| 352|0x0000000478000000, 0x0000000479000000, 0x0000000479000000|100%| O|  |TAMS 0x0000000479000000, 0x0000000478000000| Untracked 
| 353|0x0000000479000000, 0x000000047a000000, 0x000000047a000000|100%| O|  |TAMS 0x000000047a000000, 0x0000000479000000| Untracked 
| 354|0x000000047a000000, 0x000000047b000000, 0x000000047b000000|100%| O|  |TAMS 0x000000047b000000, 0x000000047a000000| Untracked 
| 355|0x000000047b000000, 0x000000047c000000, 0x000000047c000000|100%| O|  |TAMS 0x000000047c000000, 0x000000047b000000| Untracked 
| 356|0x000000047c000000, 0x000000047d000000, 0x000000047d000000|100%| O|  |TAMS 0x000000047d000000, 0x000000047c000000| Untracked 
| 357|0x000000047d000000, 0x000000047e000000, 0x000000047e000000|100%| O|  |TAMS 0x000000047e000000, 0x000000047d000000| Untracked 
| 358|0x000000047e000000, 0x000000047f000000, 0x000000047f000000|100%| O|  |TAMS 0x000000047f000000, 0x000000047e000000| Untracked 
| 359|0x000000047f000000, 0x0000000480000000, 0x0000000480000000|100%| O|  |TAMS 0x0000000480000000, 0x000000047f000000| Untracked 
| 360|0x0000000480000000, 0x0000000481000000, 0x0000000481000000|100%| O|  |TAMS 0x0000000481000000, 0x0000000480000000| Untracked 
| 361|0x0000000481000000, 0x0000000482000000, 0x0000000482000000|100%| O|  |TAMS 0x0000000482000000, 0x0000000481000000| Untracked 
| 362|0x0000000482000000, 0x0000000483000000, 0x0000000483000000|100%| O|  |TAMS 0x0000000483000000, 0x0000000482000000| Untracked 
| 363|0x0000000483000000, 0x0000000484000000, 0x0000000484000000|100%| O|  |TAMS 0x0000000484000000, 0x0000000483000000| Untracked 
| 364|0x0000000484000000, 0x0000000485000000, 0x0000000485000000|100%| O|  |TAMS 0x0000000485000000, 0x0000000484000000| Untracked 
| 365|0x0000000485000000, 0x0000000486000000, 0x0000000486000000|100%| O|  |TAMS 0x0000000486000000, 0x0000000485000000| Untracked 
| 366|0x0000000486000000, 0x0000000487000000, 0x0000000487000000|100%| O|  |TAMS 0x0000000487000000, 0x0000000486000000| Untracked 
| 367|0x0000000487000000, 0x0000000488000000, 0x0000000488000000|100%| O|  |TAMS 0x0000000488000000, 0x0000000487000000| Untracked 
| 368|0x0000000488000000, 0x0000000489000000, 0x0000000489000000|100%| O|  |TAMS 0x0000000489000000, 0x0000000488000000| Untracked 
| 369|0x0000000489000000, 0x000000048a000000, 0x000000048a000000|100%| O|  |TAMS 0x000000048a000000, 0x0000000489000000| Untracked 
| 370|0x000000048a000000, 0x000000048b000000, 0x000000048b000000|100%| O|  |TAMS 0x000000048b000000, 0x000000048a000000| Untracked 
| 371|0x000000048b000000, 0x000000048c000000, 0x000000048c000000|100%| O|  |TAMS 0x000000048c000000, 0x000000048b000000| Untracked 
| 372|0x000000048c000000, 0x000000048d000000, 0x000000048d000000|100%| O|  |TAMS 0x000000048d000000, 0x000000048c000000| Untracked 
| 373|0x000000048d000000, 0x000000048e000000, 0x000000048e000000|100%| O|  |TAMS 0x000000048e000000, 0x000000048d000000| Untracked 
| 374|0x000000048e000000, 0x000000048f000000, 0x000000048f000000|100%| O|  |TAMS 0x000000048f000000, 0x000000048e000000| Untracked 
| 375|0x000000048f000000, 0x0000000490000000, 0x0000000490000000|100%| O|  |TAMS 0x0000000490000000, 0x000000048f000000| Untracked 
| 376|0x0000000490000000, 0x0000000491000000, 0x0000000491000000|100%| O|  |TAMS 0x0000000491000000, 0x0000000490000000| Untracked 
| 377|0x0000000491000000, 0x0000000492000000, 0x0000000492000000|100%| O|  |TAMS 0x0000000492000000, 0x0000000491000000| Untracked 
| 378|0x0000000492000000, 0x0000000493000000, 0x0000000493000000|100%| O|  |TAMS 0x0000000493000000, 0x0000000492000000| Untracked 
| 379|0x0000000493000000, 0x0000000494000000, 0x0000000494000000|100%| O|  |TAMS 0x0000000494000000, 0x0000000493000000| Untracked 
| 380|0x0000000494000000, 0x0000000495000000, 0x0000000495000000|100%| O|  |TAMS 0x0000000495000000, 0x0000000494000000| Untracked 
| 381|0x0000000495000000, 0x0000000496000000, 0x0000000496000000|100%| O|  |TAMS 0x0000000496000000, 0x0000000495000000| Untracked 
| 382|0x0000000496000000, 0x0000000497000000, 0x0000000497000000|100%| O|  |TAMS 0x0000000497000000, 0x0000000496000000| Untracked 
| 383|0x0000000497000000, 0x0000000498000000, 0x0000000498000000|100%| O|  |TAMS 0x0000000498000000, 0x0000000497000000| Untracked 
| 384|0x0000000498000000, 0x0000000499000000, 0x0000000499000000|100%| O|  |TAMS 0x0000000499000000, 0x0000000498000000| Untracked 
| 385|0x0000000499000000, 0x000000049a000000, 0x000000049a000000|100%| O|  |TAMS 0x000000049a000000, 0x0000000499000000| Untracked 
| 386|0x000000049a000000, 0x000000049b000000, 0x000000049b000000|100%| O|  |TAMS 0x000000049b000000, 0x000000049a000000| Untracked 
| 387|0x000000049b000000, 0x000000049c000000, 0x000000049c000000|100%| O|  |TAMS 0x000000049c000000, 0x000000049b000000| Untracked 
| 388|0x000000049c000000, 0x000000049d000000, 0x000000049d000000|100%| O|  |TAMS 0x000000049d000000, 0x000000049c000000| Untracked 
| 389|0x000000049d000000, 0x000000049e000000, 0x000000049e000000|100%| O|  |TAMS 0x000000049e000000, 0x000000049d000000| Untracked 
| 390|0x000000049e000000, 0x000000049f000000, 0x000000049f000000|100%| O|  |TAMS 0x000000049f000000, 0x000000049e000000| Untracked 
| 391|0x000000049f000000, 0x00000004a0000000, 0x00000004a0000000|100%| O|  |TAMS 0x00000004a0000000, 0x000000049f000000| Untracked 
| 392|0x00000004a0000000, 0x00000004a1000000, 0x00000004a1000000|100%| O|  |TAMS 0x00000004a1000000, 0x00000004a0000000| Untracked 
| 393|0x00000004a1000000, 0x00000004a2000000, 0x00000004a2000000|100%| O|  |TAMS 0x00000004a2000000, 0x00000004a1000000| Untracked 
| 394|0x00000004a2000000, 0x00000004a3000000, 0x00000004a3000000|100%| O|  |TAMS 0x00000004a3000000, 0x00000004a2000000| Untracked 
| 395|0x00000004a3000000, 0x00000004a4000000, 0x00000004a4000000|100%| O|  |TAMS 0x00000004a4000000, 0x00000004a3000000| Untracked 
| 396|0x00000004a4000000, 0x00000004a5000000, 0x00000004a5000000|100%| O|  |TAMS 0x00000004a5000000, 0x00000004a4000000| Untracked 
| 397|0x00000004a5000000, 0x00000004a6000000, 0x00000004a6000000|100%| O|  |TAMS 0x00000004a6000000, 0x00000004a5000000| Untracked 
| 398|0x00000004a6000000, 0x00000004a7000000, 0x00000004a7000000|100%| O|  |TAMS 0x00000004a6000000, 0x00000004a6000000| Untracked 
| 399|0x00000004a7000000, 0x00000004a8000000, 0x00000004a8000000|100%| O|  |TAMS 0x00000004a8000000, 0x00000004a7000000| Untracked 
| 400|0x00000004a8000000, 0x00000004a9000000, 0x00000004a9000000|100%| O|  |TAMS 0x00000004a9000000, 0x00000004a8000000| Untracked 
| 401|0x00000004a9000000, 0x00000004aa000000, 0x00000004aa000000|100%| O|  |TAMS 0x00000004aa000000, 0x00000004a9000000| Untracked 
| 402|0x00000004aa000000, 0x00000004ab000000, 0x00000004ab000000|100%| O|  |TAMS 0x00000004ab000000, 0x00000004aa000000| Untracked 
| 403|0x00000004ab000000, 0x00000004ac000000, 0x00000004ac000000|100%| O|  |TAMS 0x00000004ac000000, 0x00000004ab000000| Untracked 
| 404|0x00000004ac000000, 0x00000004ad000000, 0x00000004ad000000|100%| O|  |TAMS 0x00000004ad000000, 0x00000004ac000000| Untracked 
| 405|0x00000004ad000000, 0x00000004ae000000, 0x00000004ae000000|100%| O|  |TAMS 0x00000004ae000000, 0x00000004ad000000| Untracked 
| 406|0x00000004ae000000, 0x00000004af000000, 0x00000004af000000|100%| O|  |TAMS 0x00000004af000000, 0x00000004ae000000| Untracked 
| 407|0x00000004af000000, 0x00000004b0000000, 0x00000004b0000000|100%| O|  |TAMS 0x00000004b0000000, 0x00000004af000000| Untracked 
| 408|0x00000004b0000000, 0x00000004b1000000, 0x00000004b1000000|100%| O|  |TAMS 0x00000004b1000000, 0x00000004b0000000| Untracked 
| 409|0x00000004b1000000, 0x00000004b2000000, 0x00000004b2000000|100%| O|  |TAMS 0x00000004b2000000, 0x00000004b1000000| Untracked 
| 410|0x00000004b2000000, 0x00000004b3000000, 0x00000004b3000000|100%| O|  |TAMS 0x00000004b3000000, 0x00000004b2000000| Untracked 
| 411|0x00000004b3000000, 0x00000004b4000000, 0x00000004b4000000|100%| O|  |TAMS 0x00000004b4000000, 0x00000004b3000000| Untracked 
| 412|0x00000004b4000000, 0x00000004b5000000, 0x00000004b5000000|100%| O|  |TAMS 0x00000004b5000000, 0x00000004b4000000| Untracked 
| 413|0x00000004b5000000, 0x00000004b6000000, 0x00000004b6000000|100%| O|  |TAMS 0x00000004b6000000, 0x00000004b5000000| Untracked 
| 414|0x00000004b6000000, 0x00000004b7000000, 0x00000004b7000000|100%| O|  |TAMS 0x00000004b7000000, 0x00000004b6000000| Untracked 
| 415|0x00000004b7000000, 0x00000004b8000000, 0x00000004b8000000|100%| O|  |TAMS 0x00000004b8000000, 0x00000004b7000000| Untracked 
| 416|0x00000004b8000000, 0x00000004b9000000, 0x00000004b9000000|100%| O|  |TAMS 0x00000004b9000000, 0x00000004b8000000| Untracked 
| 417|0x00000004b9000000, 0x00000004ba000000, 0x00000004ba000000|100%| O|  |TAMS 0x00000004ba000000, 0x00000004b9000000| Untracked 
| 418|0x00000004ba000000, 0x00000004bb000000, 0x00000004bb000000|100%| O|  |TAMS 0x00000004bb000000, 0x00000004ba000000| Untracked 
| 419|0x00000004bb000000, 0x00000004bc000000, 0x00000004bc000000|100%| O|  |TAMS 0x00000004bc000000, 0x00000004bb000000| Untracked 
| 420|0x00000004bc000000, 0x00000004bd000000, 0x00000004bd000000|100%| O|  |TAMS 0x00000004bd000000, 0x00000004bc000000| Untracked 
| 421|0x00000004bd000000, 0x00000004be000000, 0x00000004be000000|100%| O|  |TAMS 0x00000004be000000, 0x00000004bd000000| Untracked 
| 422|0x00000004be000000, 0x00000004bf000000, 0x00000004bf000000|100%| O|  |TAMS 0x00000004be000000, 0x00000004be000000| Untracked 
| 423|0x00000004bf000000, 0x00000004c0000000, 0x00000004c0000000|100%| O|  |TAMS 0x00000004bf000000, 0x00000004bf000000| Untracked 
| 424|0x00000004c0000000, 0x00000004c1000000, 0x00000004c1000000|100%| O|  |TAMS 0x00000004c1000000, 0x00000004c0000000| Untracked 
| 425|0x00000004c1000000, 0x00000004c2000000, 0x00000004c2000000|100%| O|  |TAMS 0x00000004c2000000, 0x00000004c1000000| Untracked 
| 426|0x00000004c2000000, 0x00000004c3000000, 0x00000004c3000000|100%| O|  |TAMS 0x00000004c3000000, 0x00000004c2000000| Untracked 
| 427|0x00000004c3000000, 0x00000004c4000000, 0x00000004c4000000|100%| O|  |TAMS 0x00000004c4000000, 0x00000004c3000000| Untracked 
| 428|0x00000004c4000000, 0x00000004c5000000, 0x00000004c5000000|100%| O|  |TAMS 0x00000004c5000000, 0x00000004c4000000| Untracked 
| 429|0x00000004c5000000, 0x00000004c6000000, 0x00000004c6000000|100%| O|  |TAMS 0x00000004c6000000, 0x00000004c5000000| Untracked 
| 430|0x00000004c6000000, 0x00000004c7000000, 0x00000004c7000000|100%| O|  |TAMS 0x00000004c7000000, 0x00000004c6000000| Untracked 
| 431|0x00000004c7000000, 0x00000004c8000000, 0x00000004c8000000|100%| O|  |TAMS 0x00000004c8000000, 0x00000004c7000000| Untracked 
| 432|0x00000004c8000000, 0x00000004c9000000, 0x00000004c9000000|100%| O|  |TAMS 0x00000004c9000000, 0x00000004c8000000| Untracked 
| 433|0x00000004c9000000, 0x00000004ca000000, 0x00000004ca000000|100%| O|  |TAMS 0x00000004ca000000, 0x00000004c9000000| Untracked 
| 434|0x00000004ca000000, 0x00000004cb000000, 0x00000004cb000000|100%| O|  |TAMS 0x00000004cb000000, 0x00000004ca000000| Untracked 
| 435|0x00000004cb000000, 0x00000004cc000000, 0x00000004cc000000|100%| O|  |TAMS 0x00000004cc000000, 0x00000004cb000000| Untracked 
| 436|0x00000004cc000000, 0x00000004cd000000, 0x00000004cd000000|100%| O|  |TAMS 0x00000004cd000000, 0x00000004cc000000| Untracked 
| 437|0x00000004cd000000, 0x00000004ce000000, 0x00000004ce000000|100%| O|  |TAMS 0x00000004ce000000, 0x00000004cd000000| Untracked 
| 438|0x00000004ce000000, 0x00000004cf000000, 0x00000004cf000000|100%| O|  |TAMS 0x00000004cf000000, 0x00000004ce000000| Untracked 
| 439|0x00000004cf000000, 0x00000004d0000000, 0x00000004d0000000|100%| O|  |TAMS 0x00000004d0000000, 0x00000004cf000000| Untracked 
| 440|0x00000004d0000000, 0x00000004d1000000, 0x00000004d1000000|100%| O|  |TAMS 0x00000004d1000000, 0x00000004d0000000| Untracked 
| 441|0x00000004d1000000, 0x00000004d2000000, 0x00000004d2000000|100%| O|  |TAMS 0x00000004d2000000, 0x00000004d1000000| Untracked 
| 442|0x00000004d2000000, 0x00000004d3000000, 0x00000004d3000000|100%| O|  |TAMS 0x00000004d3000000, 0x00000004d2000000| Untracked 
| 443|0x00000004d3000000, 0x00000004d4000000, 0x00000004d4000000|100%| O|  |TAMS 0x00000004d4000000, 0x00000004d3000000| Untracked 
| 444|0x00000004d4000000, 0x00000004d5000000, 0x00000004d5000000|100%| O|  |TAMS 0x00000004d5000000, 0x00000004d4000000| Untracked 
| 445|0x00000004d5000000, 0x00000004d6000000, 0x00000004d6000000|100%| O|  |TAMS 0x00000004d6000000, 0x00000004d5000000| Untracked 
| 446|0x00000004d6000000, 0x00000004d7000000, 0x00000004d7000000|100%| O|  |TAMS 0x00000004d7000000, 0x00000004d6000000| Untracked 
| 447|0x00000004d7000000, 0x00000004d8000000, 0x00000004d8000000|100%| O|  |TAMS 0x00000004d8000000, 0x00000004d7000000| Untracked 
| 448|0x00000004d8000000, 0x00000004d9000000, 0x00000004d9000000|100%| O|  |TAMS 0x00000004d9000000, 0x00000004d8000000| Untracked 
| 449|0x00000004d9000000, 0x00000004da000000, 0x00000004da000000|100%| O|  |TAMS 0x00000004da000000, 0x00000004d9000000| Untracked 
| 450|0x00000004da000000, 0x00000004db000000, 0x00000004db000000|100%| O|  |TAMS 0x00000004db000000, 0x00000004da000000| Untracked 
| 451|0x00000004db000000, 0x00000004dc000000, 0x00000004dc000000|100%| O|  |TAMS 0x00000004dc000000, 0x00000004db000000| Untracked 
| 452|0x00000004dc000000, 0x00000004dd000000, 0x00000004dd000000|100%| O|  |TAMS 0x00000004dd000000, 0x00000004dc000000| Untracked 
| 453|0x00000004dd000000, 0x00000004de000000, 0x00000004de000000|100%| O|  |TAMS 0x00000004de000000, 0x00000004dd000000| Untracked 
| 454|0x00000004de000000, 0x00000004df000000, 0x00000004df000000|100%| O|  |TAMS 0x00000004df000000, 0x00000004de000000| Untracked 
| 455|0x00000004df000000, 0x00000004e0000000, 0x00000004e0000000|100%| O|  |TAMS 0x00000004e0000000, 0x00000004df000000| Untracked 
| 456|0x00000004e0000000, 0x00000004e1000000, 0x00000004e1000000|100%| O|  |TAMS 0x00000004e1000000, 0x00000004e0000000| Untracked 
| 457|0x00000004e1000000, 0x00000004e2000000, 0x00000004e2000000|100%| O|  |TAMS 0x00000004e2000000, 0x00000004e1000000| Untracked 
| 458|0x00000004e2000000, 0x00000004e3000000, 0x00000004e3000000|100%| O|  |TAMS 0x00000004e3000000, 0x00000004e2000000| Untracked 
| 459|0x00000004e3000000, 0x00000004e4000000, 0x00000004e4000000|100%| O|  |TAMS 0x00000004e4000000, 0x00000004e3000000| Untracked 
| 460|0x00000004e4000000, 0x00000004e5000000, 0x00000004e5000000|100%| O|  |TAMS 0x00000004e5000000, 0x00000004e4000000| Untracked 
| 461|0x00000004e5000000, 0x00000004e6000000, 0x00000004e6000000|100%| O|  |TAMS 0x00000004e6000000, 0x00000004e5000000| Untracked 
| 462|0x00000004e6000000, 0x00000004e7000000, 0x00000004e7000000|100%| O|  |TAMS 0x00000004e7000000, 0x00000004e6000000| Untracked 
| 463|0x00000004e7000000, 0x00000004e8000000, 0x00000004e8000000|100%| O|  |TAMS 0x00000004e8000000, 0x00000004e7000000| Untracked 
| 464|0x00000004e8000000, 0x00000004e9000000, 0x00000004e9000000|100%| O|  |TAMS 0x00000004e9000000, 0x00000004e8000000| Untracked 
| 465|0x00000004e9000000, 0x00000004ea000000, 0x00000004ea000000|100%| O|  |TAMS 0x00000004ea000000, 0x00000004e9000000| Untracked 
| 466|0x00000004ea000000, 0x00000004eb000000, 0x00000004eb000000|100%| O|  |TAMS 0x00000004eb000000, 0x00000004ea000000| Untracked 
| 467|0x00000004eb000000, 0x00000004ec000000, 0x00000004ec000000|100%| O|  |TAMS 0x00000004ec000000, 0x00000004eb000000| Untracked 
| 468|0x00000004ec000000, 0x00000004ed000000, 0x00000004ed000000|100%| O|  |TAMS 0x00000004ed000000, 0x00000004ec000000| Untracked 
| 469|0x00000004ed000000, 0x00000004ee000000, 0x00000004ee000000|100%| O|  |TAMS 0x00000004ee000000, 0x00000004ed000000| Untracked 
| 470|0x00000004ee000000, 0x00000004ef000000, 0x00000004ef000000|100%| O|  |TAMS 0x00000004ef000000, 0x00000004ee000000| Untracked 
| 471|0x00000004ef000000, 0x00000004f0000000, 0x00000004f0000000|100%| O|  |TAMS 0x00000004ef000000, 0x00000004ef000000| Untracked 
| 472|0x00000004f0000000, 0x00000004f1000000, 0x00000004f1000000|100%| O|  |TAMS 0x00000004f0000000, 0x00000004f0000000| Untracked 
| 473|0x00000004f1000000, 0x00000004f2000000, 0x00000004f2000000|100%| O|  |TAMS 0x00000004f1000000, 0x00000004f1000000| Untracked 
| 474|0x00000004f2000000, 0x00000004f3000000, 0x00000004f3000000|100%| O|  |TAMS 0x00000004f2000000, 0x00000004f2000000| Untracked 
| 475|0x00000004f3000000, 0x00000004f4000000, 0x00000004f4000000|100%| O|  |TAMS 0x00000004f3000000, 0x00000004f3000000| Untracked 
| 476|0x00000004f4000000, 0x00000004f5000000, 0x00000004f5000000|100%| O|  |TAMS 0x00000004f4000000, 0x00000004f4000000| Untracked 
| 477|0x00000004f5000000, 0x00000004f6000000, 0x00000004f6000000|100%| O|  |TAMS 0x00000004f6000000, 0x00000004f5000000| Untracked 
| 478|0x00000004f6000000, 0x00000004f7000000, 0x00000004f7000000|100%| O|  |TAMS 0x00000004f7000000, 0x00000004f6000000| Untracked 
| 479|0x00000004f7000000, 0x00000004f8000000, 0x00000004f8000000|100%| O|  |TAMS 0x00000004f8000000, 0x00000004f7000000| Untracked 
| 480|0x00000004f8000000, 0x00000004f9000000, 0x00000004f9000000|100%| O|  |TAMS 0x00000004f8000000, 0x00000004f8000000| Untracked 
| 481|0x00000004f9000000, 0x00000004fa000000, 0x00000004fa000000|100%| O|  |TAMS 0x00000004f9000000, 0x00000004f9000000| Untracked 
| 482|0x00000004fa000000, 0x00000004fb000000, 0x00000004fb000000|100%| O|  |TAMS 0x00000004fa000000, 0x00000004fa000000| Untracked 
| 483|0x00000004fb000000, 0x00000004fc000000, 0x00000004fc000000|100%| O|  |TAMS 0x00000004fb000000, 0x00000004fb000000| Untracked 
| 484|0x00000004fc000000, 0x00000004fd000000, 0x00000004fd000000|100%| O|  |TAMS 0x00000004fc000000, 0x00000004fc000000| Untracked 
| 485|0x00000004fd000000, 0x00000004fe000000, 0x00000004fe000000|100%| O|  |TAMS 0x00000004fd000000, 0x00000004fd000000| Untracked 
| 486|0x00000004fe000000, 0x00000004ff000000, 0x00000004ff000000|100%| O|  |TAMS 0x00000004ff000000, 0x00000004fe000000| Untracked 
| 487|0x00000004ff000000, 0x0000000500000000, 0x0000000500000000|100%| O|  |TAMS 0x0000000500000000, 0x00000004ff000000| Untracked 
| 488|0x0000000500000000, 0x0000000501000000, 0x0000000501000000|100%| O|  |TAMS 0x0000000501000000, 0x0000000500000000| Untracked 
| 489|0x0000000501000000, 0x0000000502000000, 0x0000000502000000|100%| O|  |TAMS 0x0000000502000000, 0x0000000501000000| Untracked 
| 490|0x0000000502000000, 0x0000000503000000, 0x0000000503000000|100%| O|  |TAMS 0x0000000503000000, 0x0000000502000000| Untracked 
| 491|0x0000000503000000, 0x0000000504000000, 0x0000000504000000|100%| O|  |TAMS 0x0000000504000000, 0x0000000503000000| Untracked 
| 492|0x0000000504000000, 0x0000000505000000, 0x0000000505000000|100%| O|  |TAMS 0x0000000504000000, 0x0000000504000000| Untracked 
| 493|0x0000000505000000, 0x0000000506000000, 0x0000000506000000|100%| O|  |TAMS 0x0000000506000000, 0x0000000505000000| Untracked 
| 494|0x0000000506000000, 0x0000000507000000, 0x0000000507000000|100%| O|  |TAMS 0x0000000507000000, 0x0000000506000000| Untracked 
| 495|0x0000000507000000, 0x0000000508000000, 0x0000000508000000|100%| O|  |TAMS 0x000000050769ec00, 0x0000000507000000| Untracked 
| 496|0x0000000508000000, 0x0000000509000000, 0x0000000509000000|100%| O|  |TAMS 0x0000000508000000, 0x0000000508000000| Untracked 
| 497|0x0000000509000000, 0x000000050a000000, 0x000000050a000000|100%| O|  |TAMS 0x0000000509000000, 0x0000000509000000| Untracked 
| 498|0x000000050a000000, 0x000000050b000000, 0x000000050b000000|100%| O|  |TAMS 0x000000050a000000, 0x000000050a000000| Untracked 
| 499|0x000000050b000000, 0x000000050c000000, 0x000000050c000000|100%| O|  |TAMS 0x000000050b000000, 0x000000050b000000| Untracked 
| 500|0x000000050c000000, 0x000000050d000000, 0x000000050d000000|100%| O|  |TAMS 0x000000050c000000, 0x000000050c000000| Untracked 
| 501|0x000000050d000000, 0x000000050e000000, 0x000000050e000000|100%| O|  |TAMS 0x000000050d000000, 0x000000050d000000| Untracked 
| 502|0x000000050e000000, 0x000000050f000000, 0x000000050f000000|100%| O|  |TAMS 0x000000050e000000, 0x000000050e000000| Untracked 
| 503|0x000000050f000000, 0x0000000510000000, 0x0000000510000000|100%| O|  |TAMS 0x000000050f000000, 0x000000050f000000| Untracked 
| 504|0x0000000510000000, 0x0000000511000000, 0x0000000511000000|100%| O|  |TAMS 0x0000000510000000, 0x0000000510000000| Untracked 
| 505|0x0000000511000000, 0x0000000512000000, 0x0000000512000000|100%| O|  |TAMS 0x0000000511000000, 0x0000000511000000| Untracked 
| 506|0x0000000512000000, 0x0000000513000000, 0x0000000513000000|100%| O|  |TAMS 0x0000000512000000, 0x0000000512000000| Untracked 
| 507|0x0000000513000000, 0x0000000514000000, 0x0000000514000000|100%| O|  |TAMS 0x0000000513000000, 0x0000000513000000| Untracked 
| 508|0x0000000514000000, 0x0000000515000000, 0x0000000515000000|100%| O|  |TAMS 0x0000000514000000, 0x0000000514000000| Untracked 
| 509|0x0000000515000000, 0x0000000516000000, 0x0000000516000000|100%| O|  |TAMS 0x0000000515000000, 0x0000000515000000| Untracked 
| 510|0x0000000516000000, 0x0000000517000000, 0x0000000517000000|100%| O|  |TAMS 0x0000000516000000, 0x0000000516000000| Untracked 
| 511|0x0000000517000000, 0x0000000518000000, 0x0000000518000000|100%| O|  |TAMS 0x0000000517000000, 0x0000000517000000| Untracked 
| 512|0x0000000518000000, 0x0000000519000000, 0x0000000519000000|100%| O|  |TAMS 0x0000000518000000, 0x0000000518000000| Untracked 
| 513|0x0000000519000000, 0x000000051a000000, 0x000000051a000000|100%| O|  |TAMS 0x0000000519000000, 0x0000000519000000| Untracked 
| 514|0x000000051a000000, 0x000000051b000000, 0x000000051b000000|100%| O|  |TAMS 0x000000051a000000, 0x000000051a000000| Untracked 
| 515|0x000000051b000000, 0x000000051c000000, 0x000000051c000000|100%| O|  |TAMS 0x000000051b000000, 0x000000051b000000| Untracked 
| 516|0x000000051c000000, 0x000000051d000000, 0x000000051d000000|100%| O|  |TAMS 0x000000051c000000, 0x000000051c000000| Untracked 
| 517|0x000000051d000000, 0x000000051e000000, 0x000000051e000000|100%| O|  |TAMS 0x000000051d000000, 0x000000051d000000| Untracked 
| 518|0x000000051e000000, 0x000000051f000000, 0x000000051f000000|100%| O|  |TAMS 0x000000051e000000, 0x000000051e000000| Untracked 
| 519|0x000000051f000000, 0x0000000520000000, 0x0000000520000000|100%| O|  |TAMS 0x000000051f000000, 0x000000051f000000| Untracked 
| 520|0x0000000520000000, 0x0000000521000000, 0x0000000521000000|100%| O|  |TAMS 0x0000000520000000, 0x0000000520000000| Untracked 
| 521|0x0000000521000000, 0x0000000522000000, 0x0000000522000000|100%| O|  |TAMS 0x0000000521000000, 0x0000000521000000| Untracked 
| 522|0x0000000522000000, 0x0000000523000000, 0x0000000523000000|100%| O|  |TAMS 0x0000000522000000, 0x0000000522000000| Untracked 
| 523|0x0000000523000000, 0x0000000524000000, 0x0000000524000000|100%| O|  |TAMS 0x0000000523000000, 0x0000000523000000| Untracked 
| 524|0x0000000524000000, 0x0000000525000000, 0x0000000525000000|100%| O|  |TAMS 0x0000000524000000, 0x0000000524000000| Untracked 
| 525|0x0000000525000000, 0x0000000526000000, 0x0000000526000000|100%| O|  |TAMS 0x0000000525000000, 0x0000000525000000| Untracked 
| 526|0x0000000526000000, 0x0000000527000000, 0x0000000527000000|100%| O|  |TAMS 0x0000000526000000, 0x0000000526000000| Untracked 
| 527|0x0000000527000000, 0x0000000528000000, 0x0000000528000000|100%| O|  |TAMS 0x0000000527000000, 0x0000000527000000| Untracked 
| 528|0x0000000528000000, 0x0000000529000000, 0x0000000529000000|100%| O|  |TAMS 0x0000000528000000, 0x0000000528000000| Untracked 
| 529|0x0000000529000000, 0x000000052a000000, 0x000000052a000000|100%| O|  |TAMS 0x0000000529000000, 0x0000000529000000| Untracked 
| 530|0x000000052a000000, 0x000000052b000000, 0x000000052b000000|100%| O|  |TAMS 0x000000052a000000, 0x000000052a000000| Untracked 
| 531|0x000000052b000000, 0x000000052c000000, 0x000000052c000000|100%| O|  |TAMS 0x000000052b000000, 0x000000052b000000| Untracked 
| 532|0x000000052c000000, 0x000000052d000000, 0x000000052d000000|100%| O|  |TAMS 0x000000052c000000, 0x000000052c000000| Untracked 
| 533|0x000000052d000000, 0x000000052e000000, 0x000000052e000000|100%| O|  |TAMS 0x000000052d000000, 0x000000052d000000| Untracked 
| 534|0x000000052e000000, 0x000000052f000000, 0x000000052f000000|100%| O|  |TAMS 0x000000052e000000, 0x000000052e000000| Untracked 
| 535|0x000000052f000000, 0x0000000530000000, 0x0000000530000000|100%| O|  |TAMS 0x000000052f000000, 0x000000052f000000| Untracked 
| 536|0x0000000530000000, 0x0000000531000000, 0x0000000531000000|100%| O|  |TAMS 0x0000000530000000, 0x0000000530000000| Untracked 
| 537|0x0000000531000000, 0x0000000532000000, 0x0000000532000000|100%| O|  |TAMS 0x0000000531000000, 0x0000000531000000| Untracked 
| 538|0x0000000532000000, 0x0000000533000000, 0x0000000533000000|100%| O|  |TAMS 0x0000000532000000, 0x0000000532000000| Untracked 
| 539|0x0000000533000000, 0x0000000534000000, 0x0000000534000000|100%| O|  |TAMS 0x0000000533000000, 0x0000000533000000| Untracked 
| 540|0x0000000534000000, 0x0000000535000000, 0x0000000535000000|100%| O|  |TAMS 0x0000000534000000, 0x0000000534000000| Untracked 
| 541|0x0000000535000000, 0x0000000536000000, 0x0000000536000000|100%| O|  |TAMS 0x0000000535000000, 0x0000000535000000| Untracked 
| 542|0x0000000536000000, 0x0000000537000000, 0x0000000537000000|100%| O|  |TAMS 0x0000000536000000, 0x0000000536000000| Untracked 
| 543|0x0000000537000000, 0x0000000538000000, 0x0000000538000000|100%| O|  |TAMS 0x0000000537000000, 0x0000000537000000| Untracked 
| 544|0x0000000538000000, 0x0000000539000000, 0x0000000539000000|100%| O|  |TAMS 0x0000000538000000, 0x0000000538000000| Untracked 
| 545|0x0000000539000000, 0x000000053a000000, 0x000000053a000000|100%| O|  |TAMS 0x0000000539000000, 0x0000000539000000| Untracked 
| 546|0x000000053a000000, 0x000000053b000000, 0x000000053b000000|100%| O|  |TAMS 0x000000053a000000, 0x000000053a000000| Untracked 
| 547|0x000000053b000000, 0x000000053c000000, 0x000000053c000000|100%| O|  |TAMS 0x000000053b000000, 0x000000053b000000| Untracked 
| 548|0x000000053c000000, 0x000000053d000000, 0x000000053d000000|100%| O|  |TAMS 0x000000053c000000, 0x000000053c000000| Untracked 
| 549|0x000000053d000000, 0x000000053e000000, 0x000000053e000000|100%| O|  |TAMS 0x000000053d000000, 0x000000053d000000| Untracked 
| 550|0x000000053e000000, 0x000000053f000000, 0x000000053f000000|100%| O|  |TAMS 0x000000053e000000, 0x000000053e000000| Untracked 
| 551|0x000000053f000000, 0x0000000540000000, 0x0000000540000000|100%| O|  |TAMS 0x000000053f000000, 0x000000053f000000| Untracked 
| 552|0x0000000540000000, 0x0000000541000000, 0x0000000541000000|100%| O|  |TAMS 0x0000000540000000, 0x0000000540000000| Untracked 
| 553|0x0000000541000000, 0x0000000542000000, 0x0000000542000000|100%| O|  |TAMS 0x0000000541000000, 0x0000000541000000| Untracked 
| 554|0x0000000542000000, 0x0000000543000000, 0x0000000543000000|100%| O|  |TAMS 0x0000000542000000, 0x0000000542000000| Untracked 
| 555|0x0000000543000000, 0x0000000544000000, 0x0000000544000000|100%| O|  |TAMS 0x0000000543000000, 0x0000000543000000| Untracked 
| 556|0x0000000544000000, 0x0000000545000000, 0x0000000545000000|100%| O|  |TAMS 0x0000000544000000, 0x0000000544000000| Untracked 
| 557|0x0000000545000000, 0x0000000546000000, 0x0000000546000000|100%| O|  |TAMS 0x0000000545000000, 0x0000000545000000| Untracked 
| 558|0x0000000546000000, 0x0000000547000000, 0x0000000547000000|100%| O|  |TAMS 0x0000000546000000, 0x0000000546000000| Untracked 
| 559|0x0000000547000000, 0x0000000548000000, 0x0000000548000000|100%| O|  |TAMS 0x0000000547000000, 0x0000000547000000| Untracked 
| 560|0x0000000548000000, 0x0000000549000000, 0x0000000549000000|100%| O|  |TAMS 0x0000000548000000, 0x0000000548000000| Untracked 
| 561|0x0000000549000000, 0x000000054a000000, 0x000000054a000000|100%| O|  |TAMS 0x0000000549000000, 0x0000000549000000| Untracked 
| 562|0x000000054a000000, 0x000000054b000000, 0x000000054b000000|100%| O|  |TAMS 0x000000054a000000, 0x000000054a000000| Untracked 
| 563|0x000000054b000000, 0x000000054c000000, 0x000000054c000000|100%| O|  |TAMS 0x000000054b000000, 0x000000054b000000| Untracked 
| 564|0x000000054c000000, 0x000000054d000000, 0x000000054d000000|100%| O|  |TAMS 0x000000054c000000, 0x000000054c000000| Untracked 
| 565|0x000000054d000000, 0x000000054e000000, 0x000000054e000000|100%| O|  |TAMS 0x000000054d000000, 0x000000054d000000| Untracked 
| 566|0x000000054e000000, 0x000000054f000000, 0x000000054f000000|100%| O|  |TAMS 0x000000054e000000, 0x000000054e000000| Untracked 
| 567|0x000000054f000000, 0x0000000550000000, 0x0000000550000000|100%| O|  |TAMS 0x000000054f000000, 0x000000054f000000| Untracked 
| 568|0x0000000550000000, 0x0000000551000000, 0x0000000551000000|100%| O|  |TAMS 0x0000000550000000, 0x0000000550000000| Untracked 
| 569|0x0000000551000000, 0x0000000552000000, 0x0000000552000000|100%| O|  |TAMS 0x0000000551000000, 0x0000000551000000| Untracked 
| 570|0x0000000552000000, 0x0000000553000000, 0x0000000553000000|100%| O|  |TAMS 0x0000000552000000, 0x0000000552000000| Untracked 
| 571|0x0000000553000000, 0x0000000554000000, 0x0000000554000000|100%| O|  |TAMS 0x0000000553000000, 0x0000000553000000| Untracked 
| 572|0x0000000554000000, 0x0000000555000000, 0x0000000555000000|100%| O|  |TAMS 0x0000000554000000, 0x0000000554000000| Untracked 
| 573|0x0000000555000000, 0x0000000556000000, 0x0000000556000000|100%| O|  |TAMS 0x0000000555000000, 0x0000000555000000| Untracked 
| 574|0x0000000556000000, 0x0000000557000000, 0x0000000557000000|100%| O|  |TAMS 0x0000000556000000, 0x0000000556000000| Untracked 
| 575|0x0000000557000000, 0x0000000557db3200, 0x0000000558000000| 85%| O|  |TAMS 0x0000000557000000, 0x0000000557000000| Untracked 
| 576|0x0000000558000000, 0x0000000558000000, 0x0000000559000000|  0%| F|  |TAMS 0x0000000558000000, 0x0000000558000000| Untracked 
| 577|0x0000000559000000, 0x0000000559000000, 0x000000055a000000|  0%| F|  |TAMS 0x0000000559000000, 0x0000000559000000| Untracked 
| 578|0x000000055a000000, 0x000000055a000000, 0x000000055b000000|  0%| F|  |TAMS 0x000000055a000000, 0x000000055a000000| Untracked 
| 579|0x000000055b000000, 0x000000055b000000, 0x000000055c000000|  0%| F|  |TAMS 0x000000055b000000, 0x000000055b000000| Untracked 
| 580|0x000000055c000000, 0x000000055c000000, 0x000000055d000000|  0%| F|  |TAMS 0x000000055c000000, 0x000000055c000000| Untracked 
| 581|0x000000055d000000, 0x000000055d000000, 0x000000055e000000|  0%| F|  |TAMS 0x000000055d000000, 0x000000055d000000| Untracked 
| 582|0x000000055e000000, 0x000000055e000000, 0x000000055f000000|  0%| F|  |TAMS 0x000000055e000000, 0x000000055e000000| Untracked 
| 583|0x000000055f000000, 0x000000055f000000, 0x0000000560000000|  0%| F|  |TAMS 0x000000055f000000, 0x000000055f000000| Untracked 
| 584|0x0000000560000000, 0x0000000560000000, 0x0000000561000000|  0%| F|  |TAMS 0x0000000560000000, 0x0000000560000000| Untracked 
| 585|0x0000000561000000, 0x0000000561000000, 0x0000000562000000|  0%| F|  |TAMS 0x0000000561000000, 0x0000000561000000| Untracked 
| 586|0x0000000562000000, 0x0000000562000000, 0x0000000563000000|  0%| F|  |TAMS 0x0000000562000000, 0x0000000562000000| Untracked 
| 587|0x0000000563000000, 0x0000000563000000, 0x0000000564000000|  0%| F|  |TAMS 0x0000000563000000, 0x0000000563000000| Untracked 
| 588|0x0000000564000000, 0x0000000564000000, 0x0000000565000000|  0%| F|  |TAMS 0x0000000564000000, 0x0000000564000000| Untracked 
| 589|0x0000000565000000, 0x0000000565000000, 0x0000000566000000|  0%| F|  |TAMS 0x0000000565000000, 0x0000000565000000| Untracked 
| 590|0x0000000566000000, 0x0000000566000000, 0x0000000567000000|  0%| F|  |TAMS 0x0000000566000000, 0x0000000566000000| Untracked 
| 591|0x0000000567000000, 0x0000000567000000, 0x0000000568000000|  0%| F|  |TAMS 0x0000000567000000, 0x0000000567000000| Untracked 
| 592|0x0000000568000000, 0x0000000568000000, 0x0000000569000000|  0%| F|  |TAMS 0x0000000568000000, 0x0000000568000000| Untracked 
| 593|0x0000000569000000, 0x0000000569000000, 0x000000056a000000|  0%| F|  |TAMS 0x0000000569000000, 0x0000000569000000| Untracked 
| 594|0x000000056a000000, 0x000000056a000000, 0x000000056b000000|  0%| F|  |TAMS 0x000000056a000000, 0x000000056a000000| Untracked 
| 595|0x000000056b000000, 0x000000056b000000, 0x000000056c000000|  0%| F|  |TAMS 0x000000056b000000, 0x000000056b000000| Untracked 
| 596|0x000000056c000000, 0x000000056c000000, 0x000000056d000000|  0%| F|  |TAMS 0x000000056c000000, 0x000000056c000000| Untracked 
| 597|0x000000056d000000, 0x000000056d000000, 0x000000056e000000|  0%| F|  |TAMS 0x000000056d000000, 0x000000056d000000| Untracked 
| 598|0x000000056e000000, 0x000000056e000000, 0x000000056f000000|  0%| F|  |TAMS 0x000000056e000000, 0x000000056e000000| Untracked 
| 599|0x000000056f000000, 0x000000056f000000, 0x0000000570000000|  0%| F|  |TAMS 0x000000056f000000, 0x000000056f000000| Untracked 
| 600|0x0000000570000000, 0x0000000570000000, 0x0000000571000000|  0%| F|  |TAMS 0x0000000570000000, 0x0000000570000000| Untracked 
| 601|0x0000000571000000, 0x0000000571000000, 0x0000000572000000|  0%| F|  |TAMS 0x0000000571000000, 0x0000000571000000| Untracked 
| 602|0x0000000572000000, 0x0000000572000000, 0x0000000573000000|  0%| F|  |TAMS 0x0000000572000000, 0x0000000572000000| Untracked 
| 603|0x0000000573000000, 0x0000000573000000, 0x0000000574000000|  0%| F|  |TAMS 0x0000000573000000, 0x0000000573000000| Untracked 
| 604|0x0000000574000000, 0x0000000574000000, 0x0000000575000000|  0%| F|  |TAMS 0x0000000574000000, 0x0000000574000000| Untracked 
| 605|0x0000000575000000, 0x0000000575000000, 0x0000000576000000|  0%| F|  |TAMS 0x0000000575000000, 0x0000000575000000| Untracked 
| 606|0x0000000576000000, 0x0000000576000000, 0x0000000577000000|  0%| F|  |TAMS 0x0000000576000000, 0x0000000576000000| Untracked 
| 607|0x0000000577000000, 0x0000000577000000, 0x0000000578000000|  0%| F|  |TAMS 0x0000000577000000, 0x0000000577000000| Untracked 
| 608|0x0000000578000000, 0x0000000578000000, 0x0000000579000000|  0%| F|  |TAMS 0x0000000578000000, 0x0000000578000000| Untracked 
| 609|0x0000000579000000, 0x0000000579000000, 0x000000057a000000|  0%| F|  |TAMS 0x0000000579000000, 0x0000000579000000| Untracked 
| 610|0x000000057a000000, 0x000000057a000000, 0x000000057b000000|  0%| F|  |TAMS 0x000000057a000000, 0x000000057a000000| Untracked 
| 611|0x000000057b000000, 0x000000057b000000, 0x000000057c000000|  0%| F|  |TAMS 0x000000057b000000, 0x000000057b000000| Untracked 
| 612|0x000000057c000000, 0x000000057c000000, 0x000000057d000000|  0%| F|  |TAMS 0x000000057c000000, 0x000000057c000000| Untracked 
| 613|0x000000057d000000, 0x000000057d000000, 0x000000057e000000|  0%| F|  |TAMS 0x000000057d000000, 0x000000057d000000| Untracked 
| 614|0x000000057e000000, 0x000000057e000000, 0x000000057f000000|  0%| F|  |TAMS 0x000000057e000000, 0x000000057e000000| Untracked 
| 615|0x000000057f000000, 0x000000057f000000, 0x0000000580000000|  0%| F|  |TAMS 0x000000057f000000, 0x000000057f000000| Untracked 
| 616|0x0000000580000000, 0x0000000580000000, 0x0000000581000000|  0%| F|  |TAMS 0x0000000580000000, 0x0000000580000000| Untracked 
| 617|0x0000000581000000, 0x0000000581000000, 0x0000000582000000|  0%| F|  |TAMS 0x0000000581000000, 0x0000000581000000| Untracked 
| 618|0x0000000582000000, 0x0000000582000000, 0x0000000583000000|  0%| F|  |TAMS 0x0000000582000000, 0x0000000582000000| Untracked 
| 619|0x0000000583000000, 0x0000000583000000, 0x0000000584000000|  0%| F|  |TAMS 0x0000000583000000, 0x0000000583000000| Untracked 
| 620|0x0000000584000000, 0x0000000584000000, 0x0000000585000000|  0%| F|  |TAMS 0x0000000584000000, 0x0000000584000000| Untracked 
| 621|0x0000000585000000, 0x0000000585000000, 0x0000000586000000|  0%| F|  |TAMS 0x0000000585000000, 0x0000000585000000| Untracked 
| 622|0x0000000586000000, 0x0000000586000000, 0x0000000587000000|  0%| F|  |TAMS 0x0000000586000000, 0x0000000586000000| Untracked 
| 623|0x0000000587000000, 0x0000000587000000, 0x0000000588000000|  0%| F|  |TAMS 0x0000000587000000, 0x0000000587000000| Untracked 
| 624|0x0000000588000000, 0x0000000588000000, 0x0000000589000000|  0%| F|  |TAMS 0x0000000588000000, 0x0000000588000000| Untracked 
| 625|0x0000000589000000, 0x0000000589000000, 0x000000058a000000|  0%| F|  |TAMS 0x0000000589000000, 0x0000000589000000| Untracked 
| 626|0x000000058a000000, 0x000000058a000000, 0x000000058b000000|  0%| F|  |TAMS 0x000000058a000000, 0x000000058a000000| Untracked 
| 627|0x000000058b000000, 0x000000058b000000, 0x000000058c000000|  0%| F|  |TAMS 0x000000058b000000, 0x000000058b000000| Untracked 
| 628|0x000000058c000000, 0x000000058c000000, 0x000000058d000000|  0%| F|  |TAMS 0x000000058c000000, 0x000000058c000000| Untracked 
| 629|0x000000058d000000, 0x000000058d000000, 0x000000058e000000|  0%| F|  |TAMS 0x000000058d000000, 0x000000058d000000| Untracked 
| 630|0x000000058e000000, 0x000000058e000000, 0x000000058f000000|  0%| F|  |TAMS 0x000000058e000000, 0x000000058e000000| Untracked 
| 631|0x000000058f000000, 0x000000058f000000, 0x0000000590000000|  0%| F|  |TAMS 0x000000058f000000, 0x000000058f000000| Untracked 
| 632|0x0000000590000000, 0x0000000590000000, 0x0000000591000000|  0%| F|  |TAMS 0x0000000590000000, 0x0000000590000000| Untracked 
| 633|0x0000000591000000, 0x0000000591000000, 0x0000000592000000|  0%| F|  |TAMS 0x0000000591000000, 0x0000000591000000| Untracked 
| 634|0x0000000592000000, 0x0000000592000000, 0x0000000593000000|  0%| F|  |TAMS 0x0000000592000000, 0x0000000592000000| Untracked 
| 635|0x0000000593000000, 0x0000000593000000, 0x0000000594000000|  0%| F|  |TAMS 0x0000000593000000, 0x0000000593000000| Untracked 
| 636|0x0000000594000000, 0x0000000594000000, 0x0000000595000000|  0%| F|  |TAMS 0x0000000594000000, 0x0000000594000000| Untracked 
| 637|0x0000000595000000, 0x0000000595000000, 0x0000000596000000|  0%| F|  |TAMS 0x0000000595000000, 0x0000000595000000| Untracked 
| 638|0x0000000596000000, 0x0000000596000000, 0x0000000597000000|  0%| F|  |TAMS 0x0000000596000000, 0x0000000596000000| Untracked 
| 639|0x0000000597000000, 0x0000000597000000, 0x0000000598000000|  0%| F|  |TAMS 0x0000000597000000, 0x0000000597000000| Untracked 
| 640|0x0000000598000000, 0x0000000598000000, 0x0000000599000000|  0%| F|  |TAMS 0x0000000598000000, 0x0000000598000000| Untracked 
| 641|0x0000000599000000, 0x0000000599000000, 0x000000059a000000|  0%| F|  |TAMS 0x0000000599000000, 0x0000000599000000| Untracked 
| 642|0x000000059a000000, 0x000000059a000000, 0x000000059b000000|  0%| F|  |TAMS 0x000000059a000000, 0x000000059a000000| Untracked 
| 643|0x000000059b000000, 0x000000059b000000, 0x000000059c000000|  0%| F|  |TAMS 0x000000059b000000, 0x000000059b000000| Untracked 
| 644|0x000000059c000000, 0x000000059c000000, 0x000000059d000000|  0%| F|  |TAMS 0x000000059c000000, 0x000000059c000000| Untracked 
| 645|0x000000059d000000, 0x000000059d000000, 0x000000059e000000|  0%| F|  |TAMS 0x000000059d000000, 0x000000059d000000| Untracked 
| 646|0x000000059e000000, 0x000000059e000000, 0x000000059f000000|  0%| F|  |TAMS 0x000000059e000000, 0x000000059e000000| Untracked 
| 647|0x000000059f000000, 0x000000059f000000, 0x00000005a0000000|  0%| F|  |TAMS 0x000000059f000000, 0x000000059f000000| Untracked 
| 648|0x00000005a0000000, 0x00000005a0000000, 0x00000005a1000000|  0%| F|  |TAMS 0x00000005a0000000, 0x00000005a0000000| Untracked 
| 649|0x00000005a1000000, 0x00000005a1000000, 0x00000005a2000000|  0%| F|  |TAMS 0x00000005a1000000, 0x00000005a1000000| Untracked 
| 650|0x00000005a2000000, 0x00000005a2000000, 0x00000005a3000000|  0%| F|  |TAMS 0x00000005a2000000, 0x00000005a2000000| Untracked 
| 651|0x00000005a3000000, 0x00000005a3000000, 0x00000005a4000000|  0%| F|  |TAMS 0x00000005a3000000, 0x00000005a3000000| Untracked 
| 652|0x00000005a4000000, 0x00000005a4000000, 0x00000005a5000000|  0%| F|  |TAMS 0x00000005a4000000, 0x00000005a4000000| Untracked 
| 653|0x00000005a5000000, 0x00000005a5000000, 0x00000005a6000000|  0%| F|  |TAMS 0x00000005a5000000, 0x00000005a5000000| Untracked 
| 654|0x00000005a6000000, 0x00000005a6000000, 0x00000005a7000000|  0%| F|  |TAMS 0x00000005a6000000, 0x00000005a6000000| Untracked 
| 655|0x00000005a7000000, 0x00000005a7000000, 0x00000005a8000000|  0%| F|  |TAMS 0x00000005a7000000, 0x00000005a7000000| Untracked 
| 656|0x00000005a8000000, 0x00000005a8000000, 0x00000005a9000000|  0%| F|  |TAMS 0x00000005a8000000, 0x00000005a8000000| Untracked 
| 657|0x00000005a9000000, 0x00000005a9000000, 0x00000005aa000000|  0%| F|  |TAMS 0x00000005a9000000, 0x00000005a9000000| Untracked 
| 658|0x00000005aa000000, 0x00000005aa000000, 0x00000005ab000000|  0%| F|  |TAMS 0x00000005aa000000, 0x00000005aa000000| Untracked 
| 659|0x00000005ab000000, 0x00000005ab000000, 0x00000005ac000000|  0%| F|  |TAMS 0x00000005ab000000, 0x00000005ab000000| Untracked 
| 660|0x00000005ac000000, 0x00000005ac000000, 0x00000005ad000000|  0%| F|  |TAMS 0x00000005ac000000, 0x00000005ac000000| Untracked 
| 661|0x00000005ad000000, 0x00000005ad000000, 0x00000005ae000000|  0%| F|  |TAMS 0x00000005ad000000, 0x00000005ad000000| Untracked 
| 662|0x00000005ae000000, 0x00000005ae000000, 0x00000005af000000|  0%| F|  |TAMS 0x00000005ae000000, 0x00000005ae000000| Untracked 
| 663|0x00000005af000000, 0x00000005af000000, 0x00000005b0000000|  0%| F|  |TAMS 0x00000005af000000, 0x00000005af000000| Untracked 
| 664|0x00000005b0000000, 0x00000005b0000000, 0x00000005b1000000|  0%| F|  |TAMS 0x00000005b0000000, 0x00000005b0000000| Untracked 
| 665|0x00000005b1000000, 0x00000005b1000000, 0x00000005b2000000|  0%| F|  |TAMS 0x00000005b1000000, 0x00000005b1000000| Untracked 
| 666|0x00000005b2000000, 0x00000005b2000000, 0x00000005b3000000|  0%| F|  |TAMS 0x00000005b2000000, 0x00000005b2000000| Untracked 
| 667|0x00000005b3000000, 0x00000005b3000000, 0x00000005b4000000|  0%| F|  |TAMS 0x00000005b3000000, 0x00000005b3000000| Untracked 
| 668|0x00000005b4000000, 0x00000005b454f190, 0x00000005b5000000| 33%| S|CS|TAMS 0x00000005b4000000, 0x00000005b4000000| Complete 
| 669|0x00000005b5000000, 0x00000005b6000000, 0x00000005b6000000|100%| S|CS|TAMS 0x00000005b5000000, 0x00000005b5000000| Complete 
| 670|0x00000005b6000000, 0x00000005b7000000, 0x00000005b7000000|100%| S|CS|TAMS 0x00000005b6000000, 0x00000005b6000000| Complete 
| 671|0x00000005b7000000, 0x00000005b8000000, 0x00000005b8000000|100%| S|CS|TAMS 0x00000005b7000000, 0x00000005b7000000| Complete 
| 672|0x00000005b8000000, 0x00000005b9000000, 0x00000005b9000000|100%| S|CS|TAMS 0x00000005b8000000, 0x00000005b8000000| Complete 
| 673|0x00000005b9000000, 0x00000005ba000000, 0x00000005ba000000|100%| S|CS|TAMS 0x00000005b9000000, 0x00000005b9000000| Complete 
| 674|0x00000005ba000000, 0x00000005bb000000, 0x00000005bb000000|100%| S|CS|TAMS 0x00000005ba000000, 0x00000005ba000000| Complete 
| 675|0x00000005bb000000, 0x00000005bc000000, 0x00000005bc000000|100%| S|CS|TAMS 0x00000005bb000000, 0x00000005bb000000| Complete 
| 676|0x00000005bc000000, 0x00000005bd000000, 0x00000005bd000000|100%| S|CS|TAMS 0x00000005bc000000, 0x00000005bc000000| Complete 
| 677|0x00000005bd000000, 0x00000005be000000, 0x00000005be000000|100%| S|CS|TAMS 0x00000005bd000000, 0x00000005bd000000| Complete 
| 678|0x00000005be000000, 0x00000005bf000000, 0x00000005bf000000|100%| S|CS|TAMS 0x00000005be000000, 0x00000005be000000| Complete 
| 679|0x00000005bf000000, 0x00000005bf000000, 0x00000005c0000000|  0%| F|  |TAMS 0x00000005bf000000, 0x00000005bf000000| Untracked 
| 680|0x00000005c0000000, 0x00000005c0000000, 0x00000005c1000000|  0%| F|  |TAMS 0x00000005c0000000, 0x00000005c0000000| Untracked 
| 681|0x00000005c1000000, 0x00000005c1000000, 0x00000005c2000000|  0%| F|  |TAMS 0x00000005c1000000, 0x00000005c1000000| Untracked 
| 682|0x00000005c2000000, 0x00000005c2000000, 0x00000005c3000000|  0%| F|  |TAMS 0x00000005c2000000, 0x00000005c2000000| Untracked 
| 683|0x00000005c3000000, 0x00000005c3000000, 0x00000005c4000000|  0%| F|  |TAMS 0x00000005c3000000, 0x00000005c3000000| Untracked 
| 684|0x00000005c4000000, 0x00000005c4000000, 0x00000005c5000000|  0%| F|  |TAMS 0x00000005c4000000, 0x00000005c4000000| Untracked 
| 685|0x00000005c5000000, 0x00000005c5000000, 0x00000005c6000000|  0%| F|  |TAMS 0x00000005c5000000, 0x00000005c5000000| Untracked 
| 686|0x00000005c6000000, 0x00000005c6000000, 0x00000005c7000000|  0%| F|  |TAMS 0x00000005c6000000, 0x00000005c6000000| Untracked 
| 687|0x00000005c7000000, 0x00000005c7000000, 0x00000005c8000000|  0%| F|  |TAMS 0x00000005c7000000, 0x00000005c7000000| Untracked 
| 688|0x00000005c8000000, 0x00000005c8000000, 0x00000005c9000000|  0%| F|  |TAMS 0x00000005c8000000, 0x00000005c8000000| Untracked 
| 689|0x00000005c9000000, 0x00000005c9000000, 0x00000005ca000000|  0%| F|  |TAMS 0x00000005c9000000, 0x00000005c9000000| Untracked 
| 690|0x00000005ca000000, 0x00000005cb000000, 0x00000005cb000000|100%| S|CS|TAMS 0x00000005ca000000, 0x00000005ca000000| Complete 
| 691|0x00000005cb000000, 0x00000005cb000000, 0x00000005cc000000|  0%| F|  |TAMS 0x00000005cb000000, 0x00000005cb000000| Untracked 
| 692|0x00000005cc000000, 0x00000005cc000000, 0x00000005cd000000|  0%| F|  |TAMS 0x00000005cc000000, 0x00000005cc000000| Untracked 
| 693|0x00000005cd000000, 0x00000005cd000000, 0x00000005ce000000|  0%| F|  |TAMS 0x00000005cd000000, 0x00000005cd000000| Untracked 
| 694|0x00000005ce000000, 0x00000005ce000000, 0x00000005cf000000|  0%| F|  |TAMS 0x00000005ce000000, 0x00000005ce000000| Untracked 
| 695|0x00000005cf000000, 0x00000005cf58d1c0, 0x00000005d0000000| 34%| E|  |TAMS 0x00000005cf000000, 0x00000005cf000000| Complete 
| 696|0x00000005d0000000, 0x00000005d1000000, 0x00000005d1000000|100%| E|CS|TAMS 0x00000005d0000000, 0x00000005d0000000| Complete 
| 697|0x00000005d1000000, 0x00000005d2000000, 0x00000005d2000000|100%| E|CS|TAMS 0x00000005d1000000, 0x00000005d1000000| Complete 
| 698|0x00000005d2000000, 0x00000005d3000000, 0x00000005d3000000|100%| E|CS|TAMS 0x00000005d2000000, 0x00000005d2000000| Complete 
| 699|0x00000005d3000000, 0x00000005d4000000, 0x00000005d4000000|100%| E|CS|TAMS 0x00000005d3000000, 0x00000005d3000000| Complete 
| 700|0x00000005d4000000, 0x00000005d5000000, 0x00000005d5000000|100%| E|CS|TAMS 0x00000005d4000000, 0x00000005d4000000| Complete 
| 701|0x00000005d5000000, 0x00000005d6000000, 0x00000005d6000000|100%| E|CS|TAMS 0x00000005d5000000, 0x00000005d5000000| Complete 
| 702|0x00000005d6000000, 0x00000005d7000000, 0x00000005d7000000|100%| E|CS|TAMS 0x00000005d6000000, 0x00000005d6000000| Complete 
| 703|0x00000005d7000000, 0x00000005d8000000, 0x00000005d8000000|100%| E|CS|TAMS 0x00000005d7000000, 0x00000005d7000000| Complete 
| 704|0x00000005d8000000, 0x00000005d9000000, 0x00000005d9000000|100%| E|CS|TAMS 0x00000005d8000000, 0x00000005d8000000| Complete 
| 705|0x00000005d9000000, 0x00000005da000000, 0x00000005da000000|100%| E|CS|TAMS 0x00000005d9000000, 0x00000005d9000000| Complete 
| 706|0x00000005da000000, 0x00000005db000000, 0x00000005db000000|100%| E|CS|TAMS 0x00000005da000000, 0x00000005da000000| Complete 
| 707|0x00000005db000000, 0x00000005dc000000, 0x00000005dc000000|100%| E|CS|TAMS 0x00000005db000000, 0x00000005db000000| Complete 
| 708|0x00000005dc000000, 0x00000005dd000000, 0x00000005dd000000|100%| E|CS|TAMS 0x00000005dc000000, 0x00000005dc000000| Complete 
| 709|0x00000005dd000000, 0x00000005de000000, 0x00000005de000000|100%| E|CS|TAMS 0x00000005dd000000, 0x00000005dd000000| Complete 
| 710|0x00000005de000000, 0x00000005df000000, 0x00000005df000000|100%| E|CS|TAMS 0x00000005de000000, 0x00000005de000000| Complete 
| 711|0x00000005df000000, 0x00000005e0000000, 0x00000005e0000000|100%| E|CS|TAMS 0x00000005df000000, 0x00000005df000000| Complete 
| 712|0x00000005e0000000, 0x00000005e1000000, 0x00000005e1000000|100%| E|CS|TAMS 0x00000005e0000000, 0x00000005e0000000| Complete 
| 713|0x00000005e1000000, 0x00000005e2000000, 0x00000005e2000000|100%| E|CS|TAMS 0x00000005e1000000, 0x00000005e1000000| Complete 
| 714|0x00000005e2000000, 0x00000005e3000000, 0x00000005e3000000|100%| E|CS|TAMS 0x00000005e2000000, 0x00000005e2000000| Complete 
| 715|0x00000005e3000000, 0x00000005e4000000, 0x00000005e4000000|100%| E|CS|TAMS 0x00000005e3000000, 0x00000005e3000000| Complete 
| 716|0x00000005e4000000, 0x00000005e5000000, 0x00000005e5000000|100%| E|CS|TAMS 0x00000005e4000000, 0x00000005e4000000| Complete 
| 717|0x00000005e5000000, 0x00000005e6000000, 0x00000005e6000000|100%| E|CS|TAMS 0x00000005e5000000, 0x00000005e5000000| Complete 
| 718|0x00000005e6000000, 0x00000005e7000000, 0x00000005e7000000|100%| E|CS|TAMS 0x00000005e6000000, 0x00000005e6000000| Complete 
| 719|0x00000005e7000000, 0x00000005e8000000, 0x00000005e8000000|100%| E|CS|TAMS 0x00000005e7000000, 0x00000005e7000000| Complete 
| 720|0x00000005e8000000, 0x00000005e9000000, 0x00000005e9000000|100%| E|CS|TAMS 0x00000005e8000000, 0x00000005e8000000| Complete 
| 721|0x00000005e9000000, 0x00000005ea000000, 0x00000005ea000000|100%| E|CS|TAMS 0x00000005e9000000, 0x00000005e9000000| Complete 
| 722|0x00000005ea000000, 0x00000005eb000000, 0x00000005eb000000|100%| E|CS|TAMS 0x00000005ea000000, 0x00000005ea000000| Complete 
| 723|0x00000005eb000000, 0x00000005ec000000, 0x00000005ec000000|100%| E|CS|TAMS 0x00000005eb000000, 0x00000005eb000000| Complete 
| 724|0x00000005ec000000, 0x00000005ed000000, 0x00000005ed000000|100%| E|CS|TAMS 0x00000005ec000000, 0x00000005ec000000| Complete 
| 725|0x00000005ed000000, 0x00000005ee000000, 0x00000005ee000000|100%| E|CS|TAMS 0x00000005ed000000, 0x00000005ed000000| Complete 
| 726|0x00000005ee000000, 0x00000005ef000000, 0x00000005ef000000|100%| E|CS|TAMS 0x00000005ee000000, 0x00000005ee000000| Complete 
| 727|0x00000005ef000000, 0x00000005f0000000, 0x00000005f0000000|100%| E|CS|TAMS 0x00000005ef000000, 0x00000005ef000000| Complete 
| 728|0x00000005f0000000, 0x00000005f1000000, 0x00000005f1000000|100%| E|CS|TAMS 0x00000005f0000000, 0x00000005f0000000| Complete 
| 729|0x00000005f1000000, 0x00000005f2000000, 0x00000005f2000000|100%| E|CS|TAMS 0x00000005f1000000, 0x00000005f1000000| Complete 
| 730|0x00000005f2000000, 0x00000005f3000000, 0x00000005f3000000|100%| E|CS|TAMS 0x00000005f2000000, 0x00000005f2000000| Complete 
| 731|0x00000005f3000000, 0x00000005f4000000, 0x00000005f4000000|100%| E|CS|TAMS 0x00000005f3000000, 0x00000005f3000000| Complete 
| 732|0x00000005f4000000, 0x00000005f5000000, 0x00000005f5000000|100%| E|CS|TAMS 0x00000005f4000000, 0x00000005f4000000| Complete 
| 733|0x00000005f5000000, 0x00000005f6000000, 0x00000005f6000000|100%| E|CS|TAMS 0x00000005f5000000, 0x00000005f5000000| Complete 
| 734|0x00000005f6000000, 0x00000005f7000000, 0x00000005f7000000|100%| E|CS|TAMS 0x00000005f6000000, 0x00000005f6000000| Complete 
| 735|0x00000005f7000000, 0x00000005f8000000, 0x00000005f8000000|100%| E|CS|TAMS 0x00000005f7000000, 0x00000005f7000000| Complete 
| 736|0x00000005f8000000, 0x00000005f9000000, 0x00000005f9000000|100%| E|CS|TAMS 0x00000005f8000000, 0x00000005f8000000| Complete 
| 737|0x00000005f9000000, 0x00000005fa000000, 0x00000005fa000000|100%| E|CS|TAMS 0x00000005f9000000, 0x00000005f9000000| Complete 
| 738|0x00000005fa000000, 0x00000005fb000000, 0x00000005fb000000|100%| E|CS|TAMS 0x00000005fa000000, 0x00000005fa000000| Complete 
| 739|0x00000005fb000000, 0x00000005fc000000, 0x00000005fc000000|100%| E|CS|TAMS 0x00000005fb000000, 0x00000005fb000000| Complete 
| 740|0x00000005fc000000, 0x00000005fd000000, 0x00000005fd000000|100%| E|CS|TAMS 0x00000005fc000000, 0x00000005fc000000| Complete 
| 741|0x00000005fd000000, 0x00000005fe000000, 0x00000005fe000000|100%| E|CS|TAMS 0x00000005fd000000, 0x00000005fd000000| Complete 
| 742|0x00000005fe000000, 0x00000005ff000000, 0x00000005ff000000|100%| E|CS|TAMS 0x00000005fe000000, 0x00000005fe000000| Complete 
| 743|0x00000005ff000000, 0x0000000600000000, 0x0000000600000000|100%| E|CS|TAMS 0x00000005ff000000, 0x00000005ff000000| Complete 
| 744|0x0000000600000000, 0x0000000601000000, 0x0000000601000000|100%| E|CS|TAMS 0x0000000600000000, 0x0000000600000000| Complete 
| 745|0x0000000601000000, 0x0000000602000000, 0x0000000602000000|100%| E|CS|TAMS 0x0000000601000000, 0x0000000601000000| Complete 
| 746|0x0000000602000000, 0x0000000603000000, 0x0000000603000000|100%| E|CS|TAMS 0x0000000602000000, 0x0000000602000000| Complete 
| 747|0x0000000603000000, 0x0000000604000000, 0x0000000604000000|100%| E|CS|TAMS 0x0000000603000000, 0x0000000603000000| Complete 
| 748|0x0000000604000000, 0x0000000605000000, 0x0000000605000000|100%| E|CS|TAMS 0x0000000604000000, 0x0000000604000000| Complete 
| 749|0x0000000605000000, 0x0000000606000000, 0x0000000606000000|100%| E|CS|TAMS 0x0000000605000000, 0x0000000605000000| Complete 
| 750|0x0000000606000000, 0x0000000607000000, 0x0000000607000000|100%| E|CS|TAMS 0x0000000606000000, 0x0000000606000000| Complete 
| 751|0x0000000607000000, 0x0000000608000000, 0x0000000608000000|100%| E|CS|TAMS 0x0000000607000000, 0x0000000607000000| Complete 
| 752|0x0000000608000000, 0x0000000609000000, 0x0000000609000000|100%| E|CS|TAMS 0x0000000608000000, 0x0000000608000000| Complete 
| 753|0x0000000609000000, 0x000000060a000000, 0x000000060a000000|100%| E|CS|TAMS 0x0000000609000000, 0x0000000609000000| Complete 
| 754|0x000000060a000000, 0x000000060b000000, 0x000000060b000000|100%| E|CS|TAMS 0x000000060a000000, 0x000000060a000000| Complete 
| 755|0x000000060b000000, 0x000000060c000000, 0x000000060c000000|100%| E|CS|TAMS 0x000000060b000000, 0x000000060b000000| Complete 
| 756|0x000000060c000000, 0x000000060d000000, 0x000000060d000000|100%| E|CS|TAMS 0x000000060c000000, 0x000000060c000000| Complete 
| 757|0x000000060d000000, 0x000000060e000000, 0x000000060e000000|100%| E|CS|TAMS 0x000000060d000000, 0x000000060d000000| Complete 
| 758|0x000000060e000000, 0x000000060f000000, 0x000000060f000000|100%| E|CS|TAMS 0x000000060e000000, 0x000000060e000000| Complete 
| 759|0x000000060f000000, 0x0000000610000000, 0x0000000610000000|100%| E|CS|TAMS 0x000000060f000000, 0x000000060f000000| Complete 
| 760|0x0000000610000000, 0x0000000611000000, 0x0000000611000000|100%| E|CS|TAMS 0x0000000610000000, 0x0000000610000000| Complete 
| 761|0x0000000611000000, 0x0000000612000000, 0x0000000612000000|100%| E|CS|TAMS 0x0000000611000000, 0x0000000611000000| Complete 
| 762|0x0000000612000000, 0x0000000613000000, 0x0000000613000000|100%| E|CS|TAMS 0x0000000612000000, 0x0000000612000000| Complete 
| 763|0x0000000613000000, 0x0000000614000000, 0x0000000614000000|100%| E|CS|TAMS 0x0000000613000000, 0x0000000613000000| Complete 
| 764|0x0000000614000000, 0x0000000615000000, 0x0000000615000000|100%| E|CS|TAMS 0x0000000614000000, 0x0000000614000000| Complete 
| 765|0x0000000615000000, 0x0000000616000000, 0x0000000616000000|100%| E|CS|TAMS 0x0000000615000000, 0x0000000615000000| Complete 
| 766|0x0000000616000000, 0x0000000617000000, 0x0000000617000000|100%| E|CS|TAMS 0x0000000616000000, 0x0000000616000000| Complete 
| 767|0x0000000617000000, 0x0000000618000000, 0x0000000618000000|100%| E|CS|TAMS 0x0000000617000000, 0x0000000617000000| Complete 
| 768|0x0000000618000000, 0x0000000619000000, 0x0000000619000000|100%| E|CS|TAMS 0x0000000618000000, 0x0000000618000000| Complete 
| 769|0x0000000619000000, 0x000000061a000000, 0x000000061a000000|100%| E|CS|TAMS 0x0000000619000000, 0x0000000619000000| Complete 
| 770|0x000000061a000000, 0x000000061b000000, 0x000000061b000000|100%| E|CS|TAMS 0x000000061a000000, 0x000000061a000000| Complete 
| 771|0x000000061b000000, 0x000000061c000000, 0x000000061c000000|100%| E|CS|TAMS 0x000000061b000000, 0x000000061b000000| Complete 
| 772|0x000000061c000000, 0x000000061d000000, 0x000000061d000000|100%| E|CS|TAMS 0x000000061c000000, 0x000000061c000000| Complete 
| 773|0x000000061d000000, 0x000000061e000000, 0x000000061e000000|100%| E|CS|TAMS 0x000000061d000000, 0x000000061d000000| Complete 
| 774|0x000000061e000000, 0x000000061f000000, 0x000000061f000000|100%| E|CS|TAMS 0x000000061e000000, 0x000000061e000000| Complete 
| 775|0x000000061f000000, 0x0000000620000000, 0x0000000620000000|100%| E|CS|TAMS 0x000000061f000000, 0x000000061f000000| Complete 
| 776|0x0000000620000000, 0x0000000621000000, 0x0000000621000000|100%| E|CS|TAMS 0x0000000620000000, 0x0000000620000000| Complete 
| 777|0x0000000621000000, 0x0000000622000000, 0x0000000622000000|100%| E|CS|TAMS 0x0000000621000000, 0x0000000621000000| Complete 
| 778|0x0000000622000000, 0x0000000623000000, 0x0000000623000000|100%| E|CS|TAMS 0x0000000622000000, 0x0000000622000000| Complete 
| 779|0x0000000623000000, 0x0000000624000000, 0x0000000624000000|100%| E|CS|TAMS 0x0000000623000000, 0x0000000623000000| Complete 
| 780|0x0000000624000000, 0x0000000625000000, 0x0000000625000000|100%| E|CS|TAMS 0x0000000624000000, 0x0000000624000000| Complete 
| 781|0x0000000625000000, 0x0000000626000000, 0x0000000626000000|100%| E|CS|TAMS 0x0000000625000000, 0x0000000625000000| Complete 
| 782|0x0000000626000000, 0x0000000627000000, 0x0000000627000000|100%| E|CS|TAMS 0x0000000626000000, 0x0000000626000000| Complete 
| 783|0x0000000627000000, 0x0000000628000000, 0x0000000628000000|100%| E|CS|TAMS 0x0000000627000000, 0x0000000627000000| Complete 
| 784|0x0000000628000000, 0x0000000629000000, 0x0000000629000000|100%| E|CS|TAMS 0x0000000628000000, 0x0000000628000000| Complete 
| 785|0x0000000629000000, 0x000000062a000000, 0x000000062a000000|100%| E|CS|TAMS 0x0000000629000000, 0x0000000629000000| Complete 
| 786|0x000000062a000000, 0x000000062b000000, 0x000000062b000000|100%| E|CS|TAMS 0x000000062a000000, 0x000000062a000000| Complete 
| 787|0x000000062b000000, 0x000000062c000000, 0x000000062c000000|100%| E|CS|TAMS 0x000000062b000000, 0x000000062b000000| Complete 
| 788|0x000000062c000000, 0x000000062d000000, 0x000000062d000000|100%| E|CS|TAMS 0x000000062c000000, 0x000000062c000000| Complete 
| 789|0x000000062d000000, 0x000000062e000000, 0x000000062e000000|100%| E|CS|TAMS 0x000000062d000000, 0x000000062d000000| Complete 
| 790|0x000000062e000000, 0x000000062f000000, 0x000000062f000000|100%| E|CS|TAMS 0x000000062e000000, 0x000000062e000000| Complete 
| 791|0x000000062f000000, 0x0000000630000000, 0x0000000630000000|100%| E|CS|TAMS 0x000000062f000000, 0x000000062f000000| Complete 
| 792|0x0000000630000000, 0x0000000631000000, 0x0000000631000000|100%| E|CS|TAMS 0x0000000630000000, 0x0000000630000000| Complete 
| 793|0x0000000631000000, 0x0000000632000000, 0x0000000632000000|100%| E|CS|TAMS 0x0000000631000000, 0x0000000631000000| Complete 
| 794|0x0000000632000000, 0x0000000633000000, 0x0000000633000000|100%| E|CS|TAMS 0x0000000632000000, 0x0000000632000000| Complete 
| 795|0x0000000633000000, 0x0000000634000000, 0x0000000634000000|100%| E|CS|TAMS 0x0000000633000000, 0x0000000633000000| Complete 
| 796|0x0000000634000000, 0x0000000635000000, 0x0000000635000000|100%| E|CS|TAMS 0x0000000634000000, 0x0000000634000000| Complete 
| 797|0x0000000635000000, 0x0000000636000000, 0x0000000636000000|100%| E|CS|TAMS 0x0000000635000000, 0x0000000635000000| Complete 
| 798|0x0000000636000000, 0x0000000637000000, 0x0000000637000000|100%| E|CS|TAMS 0x0000000636000000, 0x0000000636000000| Complete 
| 799|0x0000000637000000, 0x0000000638000000, 0x0000000638000000|100%| E|CS|TAMS 0x0000000637000000, 0x0000000637000000| Complete 
| 800|0x0000000638000000, 0x0000000639000000, 0x0000000639000000|100%| E|CS|TAMS 0x0000000638000000, 0x0000000638000000| Complete 
| 801|0x0000000639000000, 0x000000063a000000, 0x000000063a000000|100%| E|CS|TAMS 0x0000000639000000, 0x0000000639000000| Complete 
| 802|0x000000063a000000, 0x000000063b000000, 0x000000063b000000|100%| E|CS|TAMS 0x000000063a000000, 0x000000063a000000| Complete 
| 803|0x000000063b000000, 0x000000063c000000, 0x000000063c000000|100%| E|CS|TAMS 0x000000063b000000, 0x000000063b000000| Complete 
| 804|0x000000063c000000, 0x000000063d000000, 0x000000063d000000|100%| E|CS|TAMS 0x000000063c000000, 0x000000063c000000| Complete 
| 805|0x000000063d000000, 0x000000063e000000, 0x000000063e000000|100%| E|CS|TAMS 0x000000063d000000, 0x000000063d000000| Complete 
| 806|0x000000063e000000, 0x000000063f000000, 0x000000063f000000|100%| E|CS|TAMS 0x000000063e000000, 0x000000063e000000| Complete 
| 807|0x000000063f000000, 0x0000000640000000, 0x0000000640000000|100%| E|CS|TAMS 0x000000063f000000, 0x000000063f000000| Complete 
| 808|0x0000000640000000, 0x0000000641000000, 0x0000000641000000|100%| E|CS|TAMS 0x0000000640000000, 0x0000000640000000| Complete 
| 809|0x0000000641000000, 0x0000000642000000, 0x0000000642000000|100%| E|CS|TAMS 0x0000000641000000, 0x0000000641000000| Complete 
| 810|0x0000000642000000, 0x0000000643000000, 0x0000000643000000|100%| E|CS|TAMS 0x0000000642000000, 0x0000000642000000| Complete 
| 811|0x0000000643000000, 0x0000000644000000, 0x0000000644000000|100%| E|CS|TAMS 0x0000000643000000, 0x0000000643000000| Complete 
| 812|0x0000000644000000, 0x0000000645000000, 0x0000000645000000|100%| E|CS|TAMS 0x0000000644000000, 0x0000000644000000| Complete 
| 813|0x0000000645000000, 0x0000000646000000, 0x0000000646000000|100%| E|CS|TAMS 0x0000000645000000, 0x0000000645000000| Complete 
| 814|0x0000000646000000, 0x0000000647000000, 0x0000000647000000|100%| E|CS|TAMS 0x0000000646000000, 0x0000000646000000| Complete 
| 815|0x0000000647000000, 0x0000000648000000, 0x0000000648000000|100%| E|CS|TAMS 0x0000000647000000, 0x0000000647000000| Complete 
| 816|0x0000000648000000, 0x0000000649000000, 0x0000000649000000|100%| E|CS|TAMS 0x0000000648000000, 0x0000000648000000| Complete 
| 817|0x0000000649000000, 0x000000064a000000, 0x000000064a000000|100%| E|CS|TAMS 0x0000000649000000, 0x0000000649000000| Complete 
| 818|0x000000064a000000, 0x000000064b000000, 0x000000064b000000|100%| E|CS|TAMS 0x000000064a000000, 0x000000064a000000| Complete 
| 819|0x000000064b000000, 0x000000064c000000, 0x000000064c000000|100%| E|CS|TAMS 0x000000064b000000, 0x000000064b000000| Complete 
| 820|0x000000064c000000, 0x000000064d000000, 0x000000064d000000|100%| E|CS|TAMS 0x000000064c000000, 0x000000064c000000| Complete 
| 821|0x000000064d000000, 0x000000064e000000, 0x000000064e000000|100%| E|CS|TAMS 0x000000064d000000, 0x000000064d000000| Complete 
| 822|0x000000064e000000, 0x000000064f000000, 0x000000064f000000|100%| E|CS|TAMS 0x000000064e000000, 0x000000064e000000| Complete 
| 823|0x000000064f000000, 0x0000000650000000, 0x0000000650000000|100%| E|CS|TAMS 0x000000064f000000, 0x000000064f000000| Complete 
| 824|0x0000000650000000, 0x0000000651000000, 0x0000000651000000|100%| E|CS|TAMS 0x0000000650000000, 0x0000000650000000| Complete 
| 825|0x0000000651000000, 0x0000000652000000, 0x0000000652000000|100%| E|CS|TAMS 0x0000000651000000, 0x0000000651000000| Complete 
| 826|0x0000000652000000, 0x0000000653000000, 0x0000000653000000|100%| E|CS|TAMS 0x0000000652000000, 0x0000000652000000| Complete 
| 827|0x0000000653000000, 0x0000000654000000, 0x0000000654000000|100%| E|CS|TAMS 0x0000000653000000, 0x0000000653000000| Complete 
| 828|0x0000000654000000, 0x0000000655000000, 0x0000000655000000|100%| E|CS|TAMS 0x0000000654000000, 0x0000000654000000| Complete 
| 829|0x0000000655000000, 0x0000000656000000, 0x0000000656000000|100%| E|CS|TAMS 0x0000000655000000, 0x0000000655000000| Complete 
| 830|0x0000000656000000, 0x0000000657000000, 0x0000000657000000|100%| E|CS|TAMS 0x0000000656000000, 0x0000000656000000| Complete 
| 831|0x0000000657000000, 0x0000000658000000, 0x0000000658000000|100%| E|CS|TAMS 0x0000000657000000, 0x0000000657000000| Complete 
| 832|0x0000000658000000, 0x0000000659000000, 0x0000000659000000|100%| E|CS|TAMS 0x0000000658000000, 0x0000000658000000| Complete 
| 833|0x0000000659000000, 0x000000065a000000, 0x000000065a000000|100%| E|CS|TAMS 0x0000000659000000, 0x0000000659000000| Complete 
| 834|0x000000065a000000, 0x000000065b000000, 0x000000065b000000|100%| E|CS|TAMS 0x000000065a000000, 0x000000065a000000| Complete 
| 835|0x000000065b000000, 0x000000065c000000, 0x000000065c000000|100%| E|CS|TAMS 0x000000065b000000, 0x000000065b000000| Complete 
| 836|0x000000065c000000, 0x000000065d000000, 0x000000065d000000|100%| E|CS|TAMS 0x000000065c000000, 0x000000065c000000| Complete 
| 837|0x000000065d000000, 0x000000065e000000, 0x000000065e000000|100%| E|CS|TAMS 0x000000065d000000, 0x000000065d000000| Complete 
| 838|0x000000065e000000, 0x000000065f000000, 0x000000065f000000|100%| E|CS|TAMS 0x000000065e000000, 0x000000065e000000| Complete 
| 839|0x000000065f000000, 0x0000000660000000, 0x0000000660000000|100%| E|CS|TAMS 0x000000065f000000, 0x000000065f000000| Complete 
| 840|0x0000000660000000, 0x0000000661000000, 0x0000000661000000|100%| E|CS|TAMS 0x0000000660000000, 0x0000000660000000| Complete 
| 841|0x0000000661000000, 0x0000000662000000, 0x0000000662000000|100%| E|CS|TAMS 0x0000000661000000, 0x0000000661000000| Complete 
| 842|0x0000000662000000, 0x0000000663000000, 0x0000000663000000|100%| E|CS|TAMS 0x0000000662000000, 0x0000000662000000| Complete 
| 843|0x0000000663000000, 0x0000000664000000, 0x0000000664000000|100%| E|CS|TAMS 0x0000000663000000, 0x0000000663000000| Complete 
| 844|0x0000000664000000, 0x0000000665000000, 0x0000000665000000|100%| E|CS|TAMS 0x0000000664000000, 0x0000000664000000| Complete 
| 845|0x0000000665000000, 0x0000000666000000, 0x0000000666000000|100%| E|CS|TAMS 0x0000000665000000, 0x0000000665000000| Complete 
| 846|0x0000000666000000, 0x0000000667000000, 0x0000000667000000|100%| E|CS|TAMS 0x0000000666000000, 0x0000000666000000| Complete 
| 847|0x0000000667000000, 0x0000000668000000, 0x0000000668000000|100%| E|CS|TAMS 0x0000000667000000, 0x0000000667000000| Complete 
| 848|0x0000000668000000, 0x0000000669000000, 0x0000000669000000|100%| E|CS|TAMS 0x0000000668000000, 0x0000000668000000| Complete 
| 849|0x0000000669000000, 0x000000066a000000, 0x000000066a000000|100%| E|CS|TAMS 0x0000000669000000, 0x0000000669000000| Complete 
| 850|0x000000066a000000, 0x000000066b000000, 0x000000066b000000|100%| E|CS|TAMS 0x000000066a000000, 0x000000066a000000| Complete 
| 851|0x000000066b000000, 0x000000066c000000, 0x000000066c000000|100%| E|CS|TAMS 0x000000066b000000, 0x000000066b000000| Complete 
| 852|0x000000066c000000, 0x000000066d000000, 0x000000066d000000|100%| E|CS|TAMS 0x000000066c000000, 0x000000066c000000| Complete 
| 853|0x000000066d000000, 0x000000066e000000, 0x000000066e000000|100%| E|CS|TAMS 0x000000066d000000, 0x000000066d000000| Complete 
| 854|0x000000066e000000, 0x000000066f000000, 0x000000066f000000|100%| E|CS|TAMS 0x000000066e000000, 0x000000066e000000| Complete 
| 855|0x000000066f000000, 0x0000000670000000, 0x0000000670000000|100%| E|CS|TAMS 0x000000066f000000, 0x000000066f000000| Complete 
| 856|0x0000000670000000, 0x0000000671000000, 0x0000000671000000|100%| E|CS|TAMS 0x0000000670000000, 0x0000000670000000| Complete 
| 857|0x0000000671000000, 0x0000000672000000, 0x0000000672000000|100%| E|CS|TAMS 0x0000000671000000, 0x0000000671000000| Complete 
| 858|0x0000000672000000, 0x0000000673000000, 0x0000000673000000|100%| E|CS|TAMS 0x0000000672000000, 0x0000000672000000| Complete 
| 859|0x0000000673000000, 0x0000000674000000, 0x0000000674000000|100%| E|CS|TAMS 0x0000000673000000, 0x0000000673000000| Complete 
| 860|0x0000000674000000, 0x0000000675000000, 0x0000000675000000|100%| E|CS|TAMS 0x0000000674000000, 0x0000000674000000| Complete 
| 861|0x0000000675000000, 0x0000000676000000, 0x0000000676000000|100%| E|  |TAMS 0x0000000675000000, 0x0000000675000000| Complete 
| 862|0x0000000676000000, 0x0000000677000000, 0x0000000677000000|100%| E|CS|TAMS 0x0000000676000000, 0x0000000676000000| Complete 
| 863|0x0000000677000000, 0x0000000678000000, 0x0000000678000000|100%| E|CS|TAMS 0x0000000677000000, 0x0000000677000000| Complete 
| 864|0x0000000678000000, 0x0000000679000000, 0x0000000679000000|100%| E|CS|TAMS 0x0000000678000000, 0x0000000678000000| Complete 
| 865|0x0000000679000000, 0x000000067a000000, 0x000000067a000000|100%| E|CS|TAMS 0x0000000679000000, 0x0000000679000000| Complete 
| 866|0x000000067a000000, 0x000000067b000000, 0x000000067b000000|100%| E|CS|TAMS 0x000000067a000000, 0x000000067a000000| Complete 
| 867|0x000000067b000000, 0x000000067c000000, 0x000000067c000000|100%| E|CS|TAMS 0x000000067b000000, 0x000000067b000000| Complete 
| 868|0x000000067c000000, 0x000000067d000000, 0x000000067d000000|100%| E|CS|TAMS 0x000000067c000000, 0x000000067c000000| Complete 
| 869|0x000000067d000000, 0x000000067e000000, 0x000000067e000000|100%| E|CS|TAMS 0x000000067d000000, 0x000000067d000000| Complete 
| 870|0x000000067e000000, 0x000000067f000000, 0x000000067f000000|100%| E|CS|TAMS 0x000000067e000000, 0x000000067e000000| Complete 
| 871|0x000000067f000000, 0x0000000680000000, 0x0000000680000000|100%| E|CS|TAMS 0x000000067f000000, 0x000000067f000000| Complete 
| 872|0x0000000680000000, 0x0000000681000000, 0x0000000681000000|100%| E|CS|TAMS 0x0000000680000000, 0x0000000680000000| Complete 
| 873|0x0000000681000000, 0x0000000682000000, 0x0000000682000000|100%| E|CS|TAMS 0x0000000681000000, 0x0000000681000000| Complete 
| 874|0x0000000682000000, 0x0000000683000000, 0x0000000683000000|100%| E|CS|TAMS 0x0000000682000000, 0x0000000682000000| Complete 
| 875|0x0000000683000000, 0x0000000684000000, 0x0000000684000000|100%| E|CS|TAMS 0x0000000683000000, 0x0000000683000000| Complete 
| 876|0x0000000684000000, 0x0000000685000000, 0x0000000685000000|100%| E|CS|TAMS 0x0000000684000000, 0x0000000684000000| Complete 
| 877|0x0000000685000000, 0x0000000686000000, 0x0000000686000000|100%| E|CS|TAMS 0x0000000685000000, 0x0000000685000000| Complete 
| 878|0x0000000686000000, 0x0000000687000000, 0x0000000687000000|100%| E|CS|TAMS 0x0000000686000000, 0x0000000686000000| Complete 
| 879|0x0000000687000000, 0x0000000688000000, 0x0000000688000000|100%| E|CS|TAMS 0x0000000687000000, 0x0000000687000000| Complete 
| 880|0x0000000688000000, 0x0000000689000000, 0x0000000689000000|100%| E|CS|TAMS 0x0000000688000000, 0x0000000688000000| Complete 
| 881|0x0000000689000000, 0x000000068a000000, 0x000000068a000000|100%| E|CS|TAMS 0x0000000689000000, 0x0000000689000000| Complete 
| 882|0x000000068a000000, 0x000000068b000000, 0x000000068b000000|100%| E|CS|TAMS 0x000000068a000000, 0x000000068a000000| Complete 
| 883|0x000000068b000000, 0x000000068c000000, 0x000000068c000000|100%| E|CS|TAMS 0x000000068b000000, 0x000000068b000000| Complete 
| 884|0x000000068c000000, 0x000000068d000000, 0x000000068d000000|100%| E|CS|TAMS 0x000000068c000000, 0x000000068c000000| Complete 
| 885|0x000000068d000000, 0x000000068e000000, 0x000000068e000000|100%| E|CS|TAMS 0x000000068d000000, 0x000000068d000000| Complete 
| 886|0x000000068e000000, 0x000000068f000000, 0x000000068f000000|100%| E|CS|TAMS 0x000000068e000000, 0x000000068e000000| Complete 
| 887|0x000000068f000000, 0x0000000690000000, 0x0000000690000000|100%| E|CS|TAMS 0x000000068f000000, 0x000000068f000000| Complete 
| 888|0x0000000690000000, 0x0000000691000000, 0x0000000691000000|100%| E|CS|TAMS 0x0000000690000000, 0x0000000690000000| Complete 
| 889|0x0000000691000000, 0x0000000692000000, 0x0000000692000000|100%| E|CS|TAMS 0x0000000691000000, 0x0000000691000000| Complete 
| 890|0x0000000692000000, 0x0000000693000000, 0x0000000693000000|100%| E|CS|TAMS 0x0000000692000000, 0x0000000692000000| Complete 
| 891|0x0000000693000000, 0x0000000694000000, 0x0000000694000000|100%| E|CS|TAMS 0x0000000693000000, 0x0000000693000000| Complete 
| 892|0x0000000694000000, 0x0000000695000000, 0x0000000695000000|100%| E|CS|TAMS 0x0000000694000000, 0x0000000694000000| Complete 
| 893|0x0000000695000000, 0x0000000696000000, 0x0000000696000000|100%| E|CS|TAMS 0x0000000695000000, 0x0000000695000000| Complete 
| 894|0x0000000696000000, 0x0000000697000000, 0x0000000697000000|100%| E|CS|TAMS 0x0000000696000000, 0x0000000696000000| Complete 
| 895|0x0000000697000000, 0x0000000698000000, 0x0000000698000000|100%| E|CS|TAMS 0x0000000697000000, 0x0000000697000000| Complete 
| 896|0x0000000698000000, 0x0000000699000000, 0x0000000699000000|100%| E|CS|TAMS 0x0000000698000000, 0x0000000698000000| Complete 
| 897|0x0000000699000000, 0x000000069a000000, 0x000000069a000000|100%| E|CS|TAMS 0x0000000699000000, 0x0000000699000000| Complete 
| 898|0x000000069a000000, 0x000000069b000000, 0x000000069b000000|100%| E|CS|TAMS 0x000000069a000000, 0x000000069a000000| Complete 
| 899|0x000000069b000000, 0x000000069c000000, 0x000000069c000000|100%| E|CS|TAMS 0x000000069b000000, 0x000000069b000000| Complete 
| 900|0x000000069c000000, 0x000000069d000000, 0x000000069d000000|100%| E|CS|TAMS 0x000000069c000000, 0x000000069c000000| Complete 
| 901|0x000000069d000000, 0x000000069e000000, 0x000000069e000000|100%| E|CS|TAMS 0x000000069d000000, 0x000000069d000000| Complete 
| 902|0x000000069e000000, 0x000000069f000000, 0x000000069f000000|100%| E|CS|TAMS 0x000000069e000000, 0x000000069e000000| Complete 
| 903|0x000000069f000000, 0x00000006a0000000, 0x00000006a0000000|100%| E|CS|TAMS 0x000000069f000000, 0x000000069f000000| Complete 
| 904|0x00000006a0000000, 0x00000006a1000000, 0x00000006a1000000|100%| E|CS|TAMS 0x00000006a0000000, 0x00000006a0000000| Complete 
| 905|0x00000006a1000000, 0x00000006a2000000, 0x00000006a2000000|100%| E|CS|TAMS 0x00000006a1000000, 0x00000006a1000000| Complete 
| 906|0x00000006a2000000, 0x00000006a3000000, 0x00000006a3000000|100%| E|CS|TAMS 0x00000006a2000000, 0x00000006a2000000| Complete 
| 907|0x00000006a3000000, 0x00000006a4000000, 0x00000006a4000000|100%| E|CS|TAMS 0x00000006a3000000, 0x00000006a3000000| Complete 
| 908|0x00000006a4000000, 0x00000006a5000000, 0x00000006a5000000|100%| E|CS|TAMS 0x00000006a4000000, 0x00000006a4000000| Complete 
| 909|0x00000006a5000000, 0x00000006a6000000, 0x00000006a6000000|100%| E|CS|TAMS 0x00000006a5000000, 0x00000006a5000000| Complete 
| 910|0x00000006a6000000, 0x00000006a7000000, 0x00000006a7000000|100%| E|CS|TAMS 0x00000006a6000000, 0x00000006a6000000| Complete 
| 911|0x00000006a7000000, 0x00000006a8000000, 0x00000006a8000000|100%| E|CS|TAMS 0x00000006a7000000, 0x00000006a7000000| Complete 
| 912|0x00000006a8000000, 0x00000006a9000000, 0x00000006a9000000|100%| E|CS|TAMS 0x00000006a8000000, 0x00000006a8000000| Complete 
| 913|0x00000006a9000000, 0x00000006aa000000, 0x00000006aa000000|100%| E|CS|TAMS 0x00000006a9000000, 0x00000006a9000000| Complete 
| 914|0x00000006aa000000, 0x00000006ab000000, 0x00000006ab000000|100%| E|CS|TAMS 0x00000006aa000000, 0x00000006aa000000| Complete 
| 915|0x00000006ab000000, 0x00000006ac000000, 0x00000006ac000000|100%| E|CS|TAMS 0x00000006ab000000, 0x00000006ab000000| Complete 
| 916|0x00000006ac000000, 0x00000006ad000000, 0x00000006ad000000|100%| E|CS|TAMS 0x00000006ac000000, 0x00000006ac000000| Complete 
| 917|0x00000006ad000000, 0x00000006ae000000, 0x00000006ae000000|100%| E|CS|TAMS 0x00000006ad000000, 0x00000006ad000000| Complete 
| 918|0x00000006ae000000, 0x00000006af000000, 0x00000006af000000|100%| E|CS|TAMS 0x00000006ae000000, 0x00000006ae000000| Complete 
| 919|0x00000006af000000, 0x00000006b0000000, 0x00000006b0000000|100%| E|CS|TAMS 0x00000006af000000, 0x00000006af000000| Complete 
| 920|0x00000006b0000000, 0x00000006b1000000, 0x00000006b1000000|100%| E|CS|TAMS 0x00000006b0000000, 0x00000006b0000000| Complete 
| 921|0x00000006b1000000, 0x00000006b2000000, 0x00000006b2000000|100%| E|CS|TAMS 0x00000006b1000000, 0x00000006b1000000| Complete 
| 922|0x00000006b2000000, 0x00000006b3000000, 0x00000006b3000000|100%| E|CS|TAMS 0x00000006b2000000, 0x00000006b2000000| Complete 
| 923|0x00000006b3000000, 0x00000006b4000000, 0x00000006b4000000|100%| E|CS|TAMS 0x00000006b3000000, 0x00000006b3000000| Complete 
| 924|0x00000006b4000000, 0x00000006b5000000, 0x00000006b5000000|100%| E|CS|TAMS 0x00000006b4000000, 0x00000006b4000000| Complete 
| 925|0x00000006b5000000, 0x00000006b6000000, 0x00000006b6000000|100%| E|CS|TAMS 0x00000006b5000000, 0x00000006b5000000| Complete 
| 926|0x00000006b6000000, 0x00000006b7000000, 0x00000006b7000000|100%| E|CS|TAMS 0x00000006b6000000, 0x00000006b6000000| Complete 

Card table byte_map: [0x000001bc8f000000,0x000001bc91740000] _byte_map_base: 0x000001bc8d740000

Marking Bits (Prev, Next): (CMBitMap*) 0x000001bcf8aa16a0, (CMBitMap*) 0x000001bcf8aa16e0
 Prev Bits: [0x000001bc93e80000, 0x000001bca7880000)
 Next Bits: [0x000001bca7880000, 0x000001bcbb280000)

Polling page: 0x000001bcf81d0000

Metaspace:

Usage:
  Non-class:    554.74 MB used.
      Class:    137.94 MB used.
       Both:    692.69 MB used.

Virtual space:
  Non-class space:      576.00 MB reserved,     556.81 MB ( 97%) committed,  9 nodes.
      Class space:        1.00 GB reserved,     139.62 MB ( 14%) committed,  1 nodes.
             Both:        1.56 GB reserved,     696.44 MB ( 44%) committed. 

Chunk freelists:
   Non-Class:  3.22 MB
       Class:  4.34 MB
        Both:  7.56 MB

MaxMetaspaceSize: unlimited
CompressedClassSpaceSize: 1.00 GB
Initial GC threshold: 21.00 MB
Current GC threshold: 1.12 GB
CDS: off
MetaspaceReclaimPolicy: balanced
 - commit_granule_bytes: 65536.
 - commit_granule_words: 8192.
 - virtual_space_node_default_size: 8388608.
 - enlarge_chunks_in_place: 1.
 - new_chunks_are_fully_committed: 0.
 - uncommit_free_chunks: 1.
 - use_allocation_guard: 0.
 - handle_deallocations: 1.


Internal statistics:

num_allocs_failed_limit: 413.
num_arena_births: 6596.
num_arena_deaths: 54.
num_vsnodes_births: 10.
num_vsnodes_deaths: 0.
num_space_committed: 11130.
num_space_uncommitted: 0.
num_chunks_returned_to_freelist: 495.
num_chunks_taken_from_freelist: 34781.
num_chunk_merges: 426.
num_chunk_splits: 25951.
num_chunks_enlarged: 20200.
num_inconsistent_stats: 0.

CodeHeap 'non-profiled nmethods': size=120000Kb used=119990Kb max_used=119999Kb free=9Kb
 bounds [0x000001bc87ad0000, 0x000001bc8f000000, 0x000001bc8f000000]
CodeHeap 'profiled nmethods': size=120000Kb used=87374Kb max_used=107361Kb free=32625Kb
 bounds [0x000001bc80000000, 0x000001bc86920000, 0x000001bc87530000]
CodeHeap 'non-nmethods': size=5760Kb used=4001Kb max_used=4108Kb free=1758Kb
 bounds [0x000001bc87530000, 0x000001bc87940000, 0x000001bc87ad0000]
 total_blobs=68336 nmethods=64251 adapters=3989
 compilation: enabled
              stopped_count=0, restarted_count=0
 full_count=0

Compilation events (20 events):
Event: 10685.650 Thread 0x000001bcff7aa7d0 105226       4       com.mojang.blaze3d.vertex.PoseStack::m_252781_ (32 bytes)
Event: 10685.653 Thread 0x000001bcff7aa7d0 nmethod 105226 0x000001bc8adb0f10 code [0x000001bc8adb10e0, 0x000001bc8adb13f0]
Event: 10691.001 Thread 0x000001bcff7aa7d0 105227       4       net.minecraft.client.renderer.entity.PiglinRenderer::m_5478_ (9 bytes)
Event: 10691.005 Thread 0x000001bcff7aa7d0 nmethod 105227 0x000001bc8adb0790 code [0x000001bc8adb0940, 0x000001bc8adb0be8]
Event: 10691.250 Thread 0x000001bcff7aa7d0 105228       4       com.jozufozu.flywheel.backend.instancing.__InstancedRenderDispatcher_tick_ClientTickEvent::invoke (9 bytes)
Event: 10691.343 Thread 0x000001bcff7aa7d0 nmethod 105228 0x000001bc853d2390 code [0x000001bc853d2680, 0x000001bc853d6630]
Event: 10691.399 Thread 0x000001bcff7aa7d0 105229       4       de.melanx.utilitix.content.__BetterMending_pullXPClient_ClientTickEvent::invoke (15 bytes)
Event: 10691.400 Thread 0x000001bcff7aa7d0 nmethod 105229 0x000001bc87e5a390 code [0x000001bc87e5a540, 0x000001bc87e5a6c8]
Event: 10694.929 Thread 0x000001bcff7aa7d0 105230       4       net.minecraft.client.KeyboardHandler::m_90893_ (1102 bytes)
Event: 10695.194 Thread 0x000001bcff7aa7d0 nmethod 105230 0x000001bc8344cb90 code [0x000001bc8344d280, 0x000001bc83452db0]
Event: 10695.283 Thread 0x000001bcff7aa7d0 105231       4       net.minecraft.world.item.CrossbowItem::m_40939_ (24 bytes)
Event: 10695.288 Thread 0x000001bcff7aa7d0 nmethod 105231 0x000001bc87e59a10 code [0x000001bc87e59bc0, 0x000001bc87e59f28]
Event: 10696.002 Thread 0x000001bcff7aa7d0 105232       4       net.minecraft.client.renderer.entity.PiglinRenderer::m_5936_ (9 bytes)
Event: 10696.011 Thread 0x000001bcff7aa7d0 nmethod 105232 0x000001bc87e58a90 code [0x000001bc87e58c80, 0x000001bc87e59148]
Event: 10696.011 Thread 0x000001bcff7aa7d0 105233       4       net.minecraft.client.model.PiglinModel::m_6973_ (17 bytes)
Event: 10696.012 Thread 0x000001bcff7aa7d0 nmethod 105233 0x000001bc8e512310 code [0x000001bc8e5124a0, 0x000001bc8e5125a8]
Event: 10697.106 Thread 0x000001bcff7aa7d0 105234       4       net.minecraft.client.model.PiglinModel::m_6973_ (611 bytes)
Event: 10697.206 Thread 0x000001bcff7aa7d0 nmethod 105234 0x000001bc84fc6590 code [0x000001bc84fc6c40, 0x000001bc84fcac50]
Event: 10697.206 Thread 0x000001bcff7aa7d0 105235       4       net.minecraft.client.model.PiglinModel::m_7884_ (10 bytes)
Event: 10697.207 Thread 0x000001bcff7aa7d0 nmethod 105235 0x000001bc87e58690 code [0x000001bc87e58840, 0x000001bc87e58968]

GC Heap History (20 events):
Event: 10273.367 GC heap before
{Heap before GC invocations=479 (full 0):
 garbage-first heap   total 15187968K, used 13425336K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 255 young (4177920K), 14 survivors (229376K)
 Metaspace       used 708165K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10273.435 GC heap after
{Heap after GC invocations=480 (full 0):
 garbage-first heap   total 15187968K, used 9471081K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 14 young (229376K), 14 survivors (229376K)
 Metaspace       used 708165K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10333.473 GC heap before
{Heap before GC invocations=480 (full 0):
 garbage-first heap   total 15187968K, used 13419625K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 255 young (4177920K), 14 survivors (229376K)
 Metaspace       used 708178K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10333.543 GC heap after
{Heap after GC invocations=481 (full 0):
 garbage-first heap   total 15187968K, used 9470130K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 14 young (229376K), 14 survivors (229376K)
 Metaspace       used 708178K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10383.562 GC heap before
{Heap before GC invocations=481 (full 0):
 garbage-first heap   total 15187968K, used 13402290K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 255 young (4177920K), 14 survivors (229376K)
 Metaspace       used 708192K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10383.635 GC heap after
{Heap after GC invocations=482 (full 0):
 garbage-first heap   total 15187968K, used 9473942K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 12 young (196608K), 12 survivors (196608K)
 Metaspace       used 708192K, committed 711936K, reserved 1638400K
  class space    used 141118K, committed 142784K, reserved 1048576K
}
Event: 10450.198 GC heap before
{Heap before GC invocations=482 (full 0):
 garbage-first heap   total 15187968K, used 13455254K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 255 young (4177920K), 12 survivors (196608K)
 Metaspace       used 708213K, committed 712000K, reserved 1638400K
  class space    used 141119K, committed 142784K, reserved 1048576K
}
Event: 10450.285 GC heap after
{Heap after GC invocations=483 (full 0):
 garbage-first heap   total 15187968K, used 9472015K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 4 young (65536K), 4 survivors (65536K)
 Metaspace       used 708213K, committed 712000K, reserved 1638400K
  class space    used 141119K, committed 142784K, reserved 1048576K
}
Event: 10512.389 GC heap before
{Heap before GC invocations=483 (full 0):
 garbage-first heap   total 15187968K, used 13568015K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 254 young (4161536K), 4 survivors (65536K)
 Metaspace       used 708351K, committed 712192K, reserved 1638400K
  class space    used 141137K, committed 142848K, reserved 1048576K
}
Event: 10512.417 GC heap after
{Heap after GC invocations=484 (full 0):
 garbage-first heap   total 15187968K, used 9478267K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 4 young (65536K), 4 survivors (65536K)
 Metaspace       used 708351K, committed 712192K, reserved 1638400K
  class space    used 141137K, committed 142848K, reserved 1048576K
}
Event: 10566.230 GC heap before
{Heap before GC invocations=484 (full 0):
 garbage-first heap   total 15187968K, used 13557883K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 254 young (4161536K), 4 survivors (65536K)
 Metaspace       used 709101K, committed 712960K, reserved 1638400K
  class space    used 141229K, committed 142976K, reserved 1048576K
}
Event: 10566.290 GC heap after
{Heap after GC invocations=485 (full 0):
 garbage-first heap   total 15187968K, used 9582482K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 10 young (163840K), 10 survivors (163840K)
 Metaspace       used 709101K, committed 712960K, reserved 1638400K
  class space    used 141229K, committed 142976K, reserved 1048576K
}
Event: 10588.013 GC heap before
{Heap before GC invocations=485 (full 0):
 garbage-first heap   total 15187968K, used 13465490K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 247 young (4046848K), 10 survivors (163840K)
 Metaspace       used 709202K, committed 713024K, reserved 1638400K
  class space    used 141236K, committed 142976K, reserved 1048576K
}
Event: 10588.066 GC heap after
{Heap after GC invocations=486 (full 0):
 garbage-first heap   total 15187968K, used 9604411K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 11 young (180224K), 11 survivors (180224K)
 Metaspace       used 709202K, committed 713024K, reserved 1638400K
  class space    used 141236K, committed 142976K, reserved 1048576K
}
Event: 10620.118 GC heap before
{Heap before GC invocations=486 (full 0):
 garbage-first heap   total 15187968K, used 13471035K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 247 young (4046848K), 11 survivors (180224K)
 Metaspace       used 709237K, committed 713088K, reserved 1638400K
  class space    used 141243K, committed 142976K, reserved 1048576K
}
Event: 10620.167 GC heap after
{Heap after GC invocations=487 (full 0):
 garbage-first heap   total 15187968K, used 9613547K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 11 young (180224K), 11 survivors (180224K)
 Metaspace       used 709237K, committed 713088K, reserved 1638400K
  class space    used 141243K, committed 142976K, reserved 1048576K
}
Event: 10654.102 GC heap before
{Heap before GC invocations=487 (full 0):
 garbage-first heap   total 15187968K, used 13480171K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 247 young (4046848K), 11 survivors (180224K)
 Metaspace       used 709247K, committed 713088K, reserved 1638400K
  class space    used 141243K, committed 142976K, reserved 1048576K
}
Event: 10654.154 GC heap after
{Heap after GC invocations=488 (full 0):
 garbage-first heap   total 15187968K, used 9612651K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 11 young (180224K), 11 survivors (180224K)
 Metaspace       used 709247K, committed 713088K, reserved 1638400K
  class space    used 141243K, committed 142976K, reserved 1048576K
}
Event: 10672.576 GC heap before
{Heap before GC invocations=488 (full 0):
 garbage-first heap   total 15187968K, used 13479275K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 247 young (4046848K), 11 survivors (180224K)
 Metaspace       used 709254K, committed 713088K, reserved 1638400K
  class space    used 141244K, committed 142976K, reserved 1048576K
}
Event: 10672.627 GC heap after
{Heap after GC invocations=489 (full 0):
 garbage-first heap   total 15187968K, used 9620488K [0x0000000318000000, 0x0000000800000000)
  region size 16384K, 12 young (196608K), 12 survivors (196608K)
 Metaspace       used 709254K, committed 713088K, reserved 1638400K
  class space    used 141244K, committed 142976K, reserved 1048576K
}

Dll operation events (16 events):
Event: 0.006 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\java.dll
Event: 0.033 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\jsvml.dll
Event: 0.216 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\net.dll
Event: 0.218 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\nio.dll
Event: 0.225 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\zip.dll
Event: 0.311 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\jimage.dll
Event: 0.587 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\verify.dll
Event: 3.492 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\management.dll
Event: 3.496 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\management_ext.dll
Event: 4.408 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\sunmscapi.dll
Event: 29.021 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl.dll
Event: 29.519 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl_stb.dll
Event: 29.655 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl_opengl.dll
Event: 57.776 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\jna7929786715547929317.dll
Event: 114.317 Loaded shared library D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\awt.dll
Event: 150.392 Loaded shared library \AppData\Local\Temp\imgui-java-natives_1722206031574\imgui-java64.dll

Deoptimization events (20 events):
Event: 10678.456 Thread 0x000001bcf8a284a0 Uncommon trap: trap_request=0xffffffbe fr.pc=0x000001bc8bf3e33c relative=0x0000000000001f3c
Event: 10678.456 Thread 0x000001bcf8a284a0 Uncommon trap: reason=profile_predicate action=maybe_recompile pc=0x000001bc8bf3e33c method=cofh.lib.client.renderer.entity.ITranslucentRenderer.renderTranslucent(Lcom/mojang/blaze3d/vertex/PoseStack;FLnet/minecraft/client/renderer/LevelRenderer;Lorg/joml
Event: 10678.456 Thread 0x000001bcf8a284a0 DEOPT PACKING pc=0x000001bc8bf3e33c sp=0x0000003c252fdf60
Event: 10678.456 Thread 0x000001bcf8a284a0 DEOPT UNPACKING pc=0x000001bc875869a3 sp=0x0000003c252fdef0 mode 2
Event: 10678.456 Thread 0x000001bcf8a284a0 Uncommon trap: trap_request=0xffffffbe fr.pc=0x000001bc8dd5793c relative=0x000000000000073c
Event: 10678.456 Thread 0x000001bcf8a284a0 Uncommon trap: reason=profile_predicate action=maybe_recompile pc=0x000001bc8dd5793c method=cofh.lib.client.renderer.entity.ITranslucentRenderer.renderTranslucent(Lcom/mojang/blaze3d/vertex/PoseStack;FLnet/minecraft/client/renderer/LevelRenderer;Lorg/joml
Event: 10678.456 Thread 0x000001bcf8a284a0 DEOPT PACKING pc=0x000001bc8dd5793c sp=0x0000003c252fdf90
Event: 10678.456 Thread 0x000001bcf8a284a0 DEOPT UNPACKING pc=0x000001bc875869a3 sp=0x0000003c252fdef8 mode 2
Event: 10678.536 Thread 0x000001bcf8a284a0 Uncommon trap: trap_request=0xffffffbe fr.pc=0x000001bc8bf3e33c relative=0x0000000000001f3c
Event: 10678.536 Thread 0x000001bcf8a284a0 Uncommon trap: reason=profile_predicate action=maybe_recompile pc=0x000001bc8bf3e33c method=cofh.lib.client.renderer.entity.ITranslucentRenderer.renderTranslucent(Lcom/mojang/blaze3d/vertex/PoseStack;FLnet/minecraft/client/renderer/LevelRenderer;Lorg/joml
Event: 10678.536 Thread 0x000001bcf8a284a0 DEOPT PACKING pc=0x000001bc8bf3e33c sp=0x0000003c252fdf60
Event: 10678.536 Thread 0x000001bcf8a284a0 DEOPT UNPACKING pc=0x000001bc875869a3 sp=0x0000003c252fdef0 mode 2
Event: 10679.281 Thread 0x000001bcf8a284a0 Uncommon trap: trap_request=0xffffffbe fr.pc=0x000001bc8dd5793c relative=0x000000000000073c
Event: 10679.281 Thread 0x000001bcf8a284a0 Uncommon trap: reason=profile_predicate action=maybe_recompile pc=0x000001bc8dd5793c method=cofh.lib.client.renderer.entity.ITranslucentRenderer.renderTranslucent(Lcom/mojang/blaze3d/vertex/PoseStack;FLnet/minecraft/client/renderer/LevelRenderer;Lorg/joml
Event: 10679.281 Thread 0x000001bcf8a284a0 DEOPT PACKING pc=0x000001bc8dd5793c sp=0x0000003c252fdf90
Event: 10679.281 Thread 0x000001bcf8a284a0 DEOPT UNPACKING pc=0x000001bc875869a3 sp=0x0000003c252fdef8 mode 2
Event: 10682.209 Thread 0x000001bcf8a284a0 Uncommon trap: trap_request=0xffffff45 fr.pc=0x000001bc87ccb79c relative=0x000000000000053c
Event: 10682.209 Thread 0x000001bcf8a284a0 Uncommon trap: reason=unstable_if action=reinterpret pc=0x000001bc87ccb79c method=java.util.concurrent.CompletableFuture$BiRelay.tryFire(I)Ljava/util/concurrent/CompletableFuture; @ 80 c2
Event: 10682.209 Thread 0x000001bcf8a284a0 DEOPT PACKING pc=0x000001bc87ccb79c sp=0x0000003c252fcb90
Event: 10682.209 Thread 0x000001bcf8a284a0 DEOPT UNPACKING pc=0x000001bc875869a3 sp=0x0000003c252fcac0 mode 2

Classes unloaded (20 events):
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e3c00 'java/lang/invoke/LambdaForm$MH+0x00000008010e3c00'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e3800 'java/lang/invoke/LambdaForm$MH+0x00000008010e3800'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e3400 'java/lang/invoke/LambdaForm$MH+0x00000008010e3400'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e2c00 'java/lang/invoke/LambdaForm$MH+0x00000008010e2c00'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e2800 'java/lang/invoke/LambdaForm$MH+0x00000008010e2800'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e2000 'java/lang/invoke/LambdaForm$MH+0x00000008010e2000'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e1800 'java/lang/invoke/LambdaForm$MH+0x00000008010e1800'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e1400 'java/lang/invoke/LambdaForm$MH+0x00000008010e1400'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e0800 'java/lang/invoke/LambdaForm$MH+0x00000008010e0800'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e0c00 'java/lang/invoke/LambdaForm$MH+0x00000008010e0c00'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010df400 'java/lang/invoke/LambdaForm$MH+0x00000008010df400'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010e0000 'java/lang/invoke/LambdaForm$MH+0x00000008010e0000'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010dec00 'java/lang/invoke/LambdaForm$MH+0x00000008010dec00'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010de800 'java/lang/invoke/LambdaForm$MH+0x00000008010de800'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010de000 'java/lang/invoke/LambdaForm$MH+0x00000008010de000'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010ddc00 'java/lang/invoke/LambdaForm$MH+0x00000008010ddc00'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010dd400 'java/lang/invoke/LambdaForm$MH+0x00000008010dd400'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010dd000 'java/lang/invoke/LambdaForm$MH+0x00000008010dd000'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010dc400 'java/lang/invoke/LambdaForm$MH+0x00000008010dc400'
Event: 103.891 Thread 0x000001bcfc69f8b0 Unloading class 0x00000008010dc000 'java/lang/invoke/LambdaForm$MH+0x00000008010dc000'

Classes redefined (0 events):
No events

Internal exceptions (20 events):
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060ceebca0}> (0x000000060ceebca0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060ceebf30}> (0x000000060ceebf30) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060cf01640}> (0x000000060cf01640) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060cf018b8}> (0x000000060cf018b8) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060cf15ff8}> (0x000000060cf15ff8) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10688.904 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x000000060cf16270}> (0x000000060cf16270) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.010 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5df98d0}> (0x00000005f5df98d0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.010 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5df9b60}> (0x00000005f5df9b60) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.011 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5e0f270}> (0x00000005f5e0f270) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.011 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5e0f4e8}> (0x00000005f5e0f4e8) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.011 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5e23c28}> (0x00000005f5e23c28) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10692.011 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005f5e23ea0}> (0x00000005f5e23ea0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de9379a0}> (0x00000005de9379a0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de937c30}> (0x00000005de937c30) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de94d510}> (0x00000005de94d510) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de94d7a0}> (0x00000005de94d7a0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de962eb0}> (0x00000005de962eb0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.058 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de963128}> (0x00000005de963128) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.059 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de977868}> (0x00000005de977868) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]
Event: 10695.059 Thread 0x000001bcf8a284a0 Exception <a 'sun/nio/fs/WindowsException'{0x00000005de977ae0}> (0x00000005de977ae0) 
thrown [s\src\hotspot\share\prims\jni.cpp, line 516]

VM Operations (20 events):
Event: 10672.576 Executing VM operation: G1CollectForAllocation
Event: 10672.627 Executing VM operation: G1CollectForAllocation done
Event: 10677.628 Executing VM operation: Cleanup
Event: 10677.629 Executing VM operation: Cleanup done
Event: 10678.629 Executing VM operation: Cleanup
Event: 10678.629 Executing VM operation: Cleanup done
Event: 10679.630 Executing VM operation: Cleanup
Event: 10679.630 Executing VM operation: Cleanup done
Event: 10681.631 Executing VM operation: Cleanup
Event: 10681.631 Executing VM operation: Cleanup done
Event: 10682.631 Executing VM operation: Cleanup
Event: 10682.631 Executing VM operation: Cleanup done
Event: 10684.632 Executing VM operation: Cleanup
Event: 10684.632 Executing VM operation: Cleanup done
Event: 10690.753 Executing VM operation: HandshakeAllThreads
Event: 10690.753 Executing VM operation: HandshakeAllThreads done
Event: 10695.756 Executing VM operation: Cleanup
Event: 10695.756 Executing VM operation: Cleanup done
Event: 10696.757 Executing VM operation: Cleanup
Event: 10696.757 Executing VM operation: Cleanup done

Events (20 events):
Event: 10676.889 Thread 0x000001bdd57f1f60 Thread exited: 0x000001bdd57f1f60
Event: 10676.891 Thread 0x000001be747e2600 Thread exited: 0x000001be747e2600
Event: 10676.891 Thread 0x000001bd930d8b90 Thread added: 0x000001bd930d8b90
Event: 10678.019 Thread 0x000001bde21a7110 Thread exited: 0x000001bde21a7110
Event: 10678.019 Thread 0x000001bde21a9480 Thread exited: 0x000001bde21a9480
Event: 10678.024 Thread 0x000001bdd3182f10 Thread added: 0x000001bdd3182f10
Event: 10678.025 Thread 0x000001bd2fb62a70 Thread added: 0x000001bd2fb62a70
Event: 10678.033 Thread 0x000001bdd3182f10 Thread exited: 0x000001bdd3182f10
Event: 10678.033 Thread 0x000001bd2fb62a70 Thread exited: 0x000001bd2fb62a70
Event: 10678.035 Thread 0x000001bd2fb62a70 Thread added: 0x000001bd2fb62a70
Event: 10678.038 Thread 0x000001bdd31810b0 Thread added: 0x000001bdd31810b0
Event: 10678.045 Thread 0x000001bdd31810b0 Thread exited: 0x000001bdd31810b0
Event: 10678.045 Thread 0x000001bd2fb62a70 Thread exited: 0x000001bd2fb62a70
Event: 10678.048 Thread 0x000001bdd31810b0 Thread added: 0x000001bdd31810b0
Event: 10678.051 Thread 0x000001bdd3182f10 Thread added: 0x000001bdd3182f10
Event: 10679.131 Thread 0x000001beb1e4ea60 Thread added: 0x000001beb1e4ea60
Event: 10687.080 Thread 0x000001be747e20f0 Thread exited: 0x000001be747e20f0
Event: 10687.115 Thread 0x000001bdd57ef1d0 Thread exited: 0x000001bdd57ef1d0
Event: 10687.118 Thread 0x000001bcc3812480 Thread exited: 0x000001bcc3812480
Event: 10687.120 Thread 0x000001bdd2e109b0 Thread exited: 0x000001bdd2e109b0


Dynamic libraries:
0x00007ff7034f0000 - 0x00007ff7034fe000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\javaw.exe
0x00007ff9c2ef0000 - 0x00007ff9c30e8000 	C:\Windows\SYSTEM32\ntdll.dll
0x00007ff9c2cd0000 - 0x00007ff9c2d91000 	C:\Windows\System32\KERNEL32.DLL
0x00007ff9c05a0000 - 0x00007ff9c0896000 	C:\Windows\System32\KERNELBASE.dll
0x00007ff9c0e20000 - 0x00007ff9c0f20000 	C:\Windows\System32\ucrtbase.dll
0x00007ff9b62a0000 - 0x00007ff9b62b7000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\jli.dll
0x00007ff9a9470000 - 0x00007ff9a948b000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\VCRUNTIME140.dll
0x00007ff9c2a00000 - 0x00007ff9c2b9f000 	C:\Windows\System32\USER32.dll
0x00007ff9c08a0000 - 0x00007ff9c08c2000 	C:\Windows\System32\win32u.dll
0x00007ff9aab90000 - 0x00007ff9aae2a000 	C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.4355_none_60b8b9eb71f62e16\COMCTL32.dll
0x00007ff9c17b0000 - 0x00007ff9c184e000 	C:\Windows\System32\msvcrt.dll
0x00007ff9c1e10000 - 0x00007ff9c1e3b000 	C:\Windows\System32\GDI32.dll
0x00007ff9c09a0000 - 0x00007ff9c0ab7000 	C:\Windows\System32\gdi32full.dll
0x00007ff9c0900000 - 0x00007ff9c099d000 	C:\Windows\System32\msvcp_win.dll
0x00007ff9c1f00000 - 0x00007ff9c1f2f000 	C:\Windows\System32\IMM32.DLL
0x00007ff9bc9a0000 - 0x00007ff9bc9ac000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\vcruntime140_1.dll
0x00007ff99f230000 - 0x00007ff99f2bd000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\msvcp140.dll
0x00007ff989030000 - 0x00007ff989c95000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\server\jvm.dll
0x00007ff9c2e00000 - 0x00007ff9c2eb0000 	C:\Windows\System32\ADVAPI32.dll
0x00007ff9c1490000 - 0x00007ff9c1530000 	C:\Windows\System32\sechost.dll
0x00007ff9c2ba0000 - 0x00007ff9c2cc3000 	C:\Windows\System32\RPCRT4.dll
0x00007ff9c08d0000 - 0x00007ff9c08f7000 	C:\Windows\System32\bcrypt.dll
0x00007ff9c03f0000 - 0x00007ff9c043b000 	C:\Windows\SYSTEM32\POWRPROF.dll
0x00007ff9b49b0000 - 0x00007ff9b49d7000 	C:\Windows\SYSTEM32\WINMM.dll
0x00007ff9b63a0000 - 0x00007ff9b63a9000 	C:\Windows\SYSTEM32\WSOCK32.dll
0x00007ff9c1b50000 - 0x00007ff9c1bbb000 	C:\Windows\System32\WS2_32.dll
0x00007ff9b9ad0000 - 0x00007ff9b9ada000 	C:\Windows\SYSTEM32\VERSION.dll
0x00007ff9c03d0000 - 0x00007ff9c03e2000 	C:\Windows\SYSTEM32\UMPDC.dll
0x00007ff9be440000 - 0x00007ff9be452000 	C:\Windows\SYSTEM32\kernel.appcore.dll
0x00007ff9b6290000 - 0x00007ff9b629a000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\jimage.dll
0x00007ff9b8f00000 - 0x00007ff9b90e4000 	C:\Windows\SYSTEM32\DBGHELP.DLL
0x00007ff99ed40000 - 0x00007ff99ed74000 	C:\Windows\SYSTEM32\dbgcore.DLL
0x00007ff9c0ce0000 - 0x00007ff9c0d62000 	C:\Windows\System32\bcryptPrimitives.dll
0x00007ff9a8f00000 - 0x00007ff9a8f25000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\java.dll
0x00007ff9a7e60000 - 0x00007ff9a7e78000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\zip.dll
0x00007ff99d990000 - 0x00007ff99da67000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\jsvml.dll
0x00007ff9c1f30000 - 0x00007ff9c269c000 	C:\Windows\System32\SHELL32.dll
0x00007ff9be640000 - 0x00007ff9bedde000 	C:\Windows\SYSTEM32\windows.storage.dll
0x00007ff9c26a0000 - 0x00007ff9c29f3000 	C:\Windows\System32\combase.dll
0x00007ff9bfef0000 - 0x00007ff9bff1e000 	C:\Windows\SYSTEM32\Wldp.dll
0x00007ff9c19e0000 - 0x00007ff9c1aad000 	C:\Windows\System32\OLEAUT32.dll
0x00007ff9c1e40000 - 0x00007ff9c1eed000 	C:\Windows\System32\SHCORE.dll
0x00007ff9c1540000 - 0x00007ff9c1595000 	C:\Windows\System32\shlwapi.dll
0x00007ff9c04d0000 - 0x00007ff9c04f4000 	C:\Windows\SYSTEM32\profapi.dll
0x00007ff9a7e40000 - 0x00007ff9a7e59000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\net.dll
0x00007ff9bb580000 - 0x00007ff9bb68a000 	C:\Windows\SYSTEM32\WINHTTP.dll
0x00007ff9bfc50000 - 0x00007ff9bfcba000 	C:\Windows\system32\mswsock.dll
0x00007ff9a7e20000 - 0x00007ff9a7e36000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\nio.dll
0x00007ff9b6260000 - 0x00007ff9b6270000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\verify.dll
0x00007ff9bc930000 - 0x00007ff9bc939000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\management.dll
0x00007ff9b6320000 - 0x00007ff9b632b000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\management_ext.dll
0x00007ff9c1ef0000 - 0x00007ff9c1ef8000 	C:\Windows\System32\PSAPI.DLL
0x00007ff9bc600000 - 0x00007ff9bc617000 	C:\Windows\system32\napinsp.dll
0x00007ff9b6640000 - 0x00007ff9b665b000 	C:\Windows\system32\pnrpnsp.dll
0x00007ff9bce70000 - 0x00007ff9bce85000 	C:\Windows\system32\wshbth.dll
0x00007ff9bc750000 - 0x00007ff9bc76d000 	C:\Windows\system32\NLAapi.dll
0x00007ff9bf930000 - 0x00007ff9bf96b000 	C:\Windows\SYSTEM32\IPHLPAPI.DLL
0x00007ff9bf970000 - 0x00007ff9bfa3a000 	C:\Windows\SYSTEM32\DNSAPI.dll
0x00007ff9c1ab0000 - 0x00007ff9c1ab8000 	C:\Windows\System32\NSI.dll
0x00007ff9b6620000 - 0x00007ff9b6632000 	C:\Windows\System32\winrnr.dll
0x00007ff9a6960000 - 0x00007ff9a696a000 	C:\Windows\System32\rasadhlp.dll
0x00007ff9b8630000 - 0x00007ff9b86b0000 	C:\Windows\System32\fwpuclnt.dll
0x00007ff9b6310000 - 0x00007ff9b631e000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\sunmscapi.dll
0x00007ff9c0b10000 - 0x00007ff9c0c6e000 	C:\Windows\System32\CRYPT32.dll
0x00007ff9bff60000 - 0x00007ff9bff89000 	C:\Windows\SYSTEM32\ncrypt.dll
0x00007ff9bff20000 - 0x00007ff9bff5b000 	C:\Windows\SYSTEM32\NTASN1.dll
0x00007ff99db10000 - 0x00007ff99db85000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl.dll
0x00007ff99d880000 - 0x00007ff99d8e1000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\glfw.dll
0x00007ff9a7d90000 - 0x00007ff9a7dd5000 	C:\Windows\SYSTEM32\dinput8.dll
0x00007ff9795e0000 - 0x00007ff9795f1000 	C:\Windows\SYSTEM32\xinput1_4.dll
0x00007ff9c0ac0000 - 0x00007ff9c0b0e000 	C:\Windows\System32\cfgmgr32.dll
0x00007ff9c0250000 - 0x00007ff9c0283000 	C:\Windows\SYSTEM32\DEVOBJ.dll
0x00007ff9be150000 - 0x00007ff9be17f000 	C:\Windows\SYSTEM32\dwmapi.dll
0x00007ff9b5680000 - 0x00007ff9b57d2000 	C:\Windows\SYSTEM32\inputhost.dll
0x00007ff9bb480000 - 0x00007ff9bb572000 	C:\Windows\SYSTEM32\CoreMessaging.dll
0x00007ff9bd930000 - 0x00007ff9bda26000 	C:\Windows\SYSTEM32\PROPSYS.dll
0x00007ff9bb120000 - 0x00007ff9bb47b000 	C:\Windows\SYSTEM32\CoreUIComponents.dll
0x00007ff9bcf30000 - 0x00007ff9bd087000 	C:\Windows\SYSTEM32\wintypes.dll
0x00007ff9bf6b0000 - 0x00007ff9bf6e3000 	C:\Windows\SYSTEM32\ntmarta.dll
0x00007ff9bdf40000 - 0x00007ff9bdfde000 	C:\Windows\system32\uxtheme.dll
0x00007ff9c1cf0000 - 0x00007ff9c1e04000 	C:\Windows\System32\MSCTF.dll
0x00007ff96e220000 - 0x00007ff96e348000 	C:\Windows\SYSTEM32\opengl32.dll
0x00007ff96f570000 - 0x00007ff96f59c000 	C:\Windows\SYSTEM32\GLU32.dll
0x00007ff9c1850000 - 0x00007ff9c18f9000 	C:\Windows\System32\clbcatq.dll
0x00007ff947040000 - 0x00007ff949628000 	C:\Windows\System32\DriverStore\FileRepository\nvmdi.inf_amd64_7b5ca18eebabd2c0\nvoglv64.dll
0x00007ff9c0f20000 - 0x00007ff9c138e000 	C:\Windows\System32\SETUPAPI.dll
0x00007ff9c1bc0000 - 0x00007ff9c1ceb000 	C:\Windows\System32\ole32.dll
0x00007ff9bc190000 - 0x00007ff9bc1a4000 	C:\Windows\SYSTEM32\WTSAPI32.dll
0x00007ff9c0080000 - 0x00007ff9c0092000 	C:\Windows\SYSTEM32\msasn1.dll
0x00007ff9b9a90000 - 0x00007ff9b9ac1000 	C:\Windows\SYSTEM32\cryptnet.dll
0x00007ff9bfe40000 - 0x00007ff9bfe4c000 	C:\Windows\SYSTEM32\cryptbase.dll
0x00007ff9b91f0000 - 0x00007ff9b9337000 	C:\Windows\SYSTEM32\drvstore.dll
0x00007ff9c0c70000 - 0x00007ff9c0cd9000 	C:\Windows\System32\WINTRUST.dll
0x00007ff9c1470000 - 0x00007ff9c148d000 	C:\Windows\System32\imagehlp.dll
0x00007ff9bfe50000 - 0x00007ff9bfe68000 	C:\Windows\SYSTEM32\CRYPTSP.dll
0x00007ff9bf570000 - 0x00007ff9bf5a4000 	C:\Windows\system32\rsaenh.dll
0x00007ff9b1510000 - 0x00007ff9b34fe000 	C:\Windows\System32\DriverStore\FileRepository\nvmdi.inf_amd64_7b5ca18eebabd2c0\nvgpucomp64.dll
0x00007ff9b6560000 - 0x00007ff9b659b000 	C:\Windows\SYSTEM32\dxcore.dll
0x00007ff9783a0000 - 0x00007ff978670000 	C:\Windows\system32\nvspcap64.dll
0x00007ff9c02c0000 - 0x00007ff9c031b000 	C:\Windows\SYSTEM32\WINSTA.dll
0x00007ff98d2b0000 - 0x00007ff98d509000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\jemalloc.dll
0x00007ff99d6e0000 - 0x00007ff99d761000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl_stb.dll
0x00007ff9b57e0000 - 0x00007ff9b58d9000 	C:\Windows\SYSTEM32\textinputframework.dll
0x00007ff99ddc0000 - 0x00007ff99de1d000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\lwjgl_opengl.dll
0x00007ff9a3540000 - 0x00007ff9a3593000 	C:\Windows\SYSTEM32\pdh.dll
0x00007ff9bca00000 - 0x00007ff9bca0f000 	C:\Windows\System32\perfproc.dll
0x00007ff9a7d80000 - 0x00007ff9a7d8f000 	C:\Windows\System32\perfos.dll
0x00007ff9c0480000 - 0x00007ff9c04ae000 	C:\Windows\SYSTEM32\USERENV.dll
0x00007ff9bbd40000 - 0x00007ff9bbd57000 	C:\Windows\SYSTEM32\dhcpcsvc6.DLL
0x00007ff9bc100000 - 0x00007ff9bc11d000 	C:\Windows\SYSTEM32\dhcpcsvc.DLL
0x00007ff99d950000 - 0x00007ff99d990000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\jna7929786715547929317.dll
0x00007ff9b7c00000 - 0x00007ff9b7c1f000 	C:\Windows\SYSTEM32\amsi.dll
0x00007ff9a7990000 - 0x00007ff9a7a11000 	C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24060.7-0\MpOav.dll
0x00007ff9bcad0000 - 0x00007ff9bcb7e000 	C:\Windows\SYSTEM32\mscms.dll
0x00007ff9bca80000 - 0x00007ff9bca91000 	C:\Windows\SYSTEM32\ColorAdapterClient.dll
0x00007ff993f70000 - 0x00007ff993fb6000 	C:\Windows\SYSTEM32\icm32.dll
0x00007ff9b6340000 - 0x00007ff9b6347000 	C:\Windows\system32\wshunix.dll
0x00007ff98a200000 - 0x00007ff98a38f000 	D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\awt.dll
0x00007ff9bb810000 - 0x00007ff9bb8a4000 	C:\Windows\SYSTEM32\apphelp.dll
0x00007ff988c50000 - 0x00007ff988de7000 	D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0\OpenAL.dll
0x00007ff9bb8b0000 - 0x00007ff9bb935000 	C:\Windows\System32\MMDevApi.dll
0x00007ff98f9a0000 - 0x00007ff98fb2e000 	C:\Windows\System32\Speech\Common\sapi.dll
0x00007ff974bd0000 - 0x00007ff974bee000 	C:\Windows\SYSTEM32\MSACM32.dll
0x00007ff9b62e0000 - 0x00007ff9b62eb000 	C:\Windows\SYSTEM32\msdmo.dll
0x00007ff9a5800000 - 0x00007ff9a5826000 	C:\Windows\SYSTEM32\winmmbase.dll
0x0000000064a00000 - 0x000000006578a000 	\AppData\Local\Temp\imgui-java-natives_1722206031574\imgui-java64.dll
0x00007ff9bbb40000 - 0x00007ff9bbcc1000 	C:\Windows\SYSTEM32\AUDIOSES.DLL
0x00007ff9be050000 - 0x00007ff9be064000 	C:\Windows\SYSTEM32\resourcepolicyclient.dll

dbghelp: loaded successfully - version: 4.0.5 - missing functions: none
symbol engine: initialized successfully - sym options: 0x614 - pdb path: .;D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin;C:\Windows\SYSTEM32;C:\Windows\WinSxS\amd64_microsoft.windows.common-controls_6595b64144ccf1df_6.0.19041.4355_none_60b8b9eb71f62e16;D:\MINE2024\curseforge\minecraft\Install\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\server;D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0;C:\Windows\System32\DriverStore\FileRepository\nvmdi.inf_amd64_7b5ca18eebabd2c0;C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.24060.7-0;C:\Windows\System32\Speech\Common;\AppData\Local\Temp\imgui-java-natives_1722206031574

VM Arguments:
jvm_args: -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Xss1M -Djava.library.path=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Djna.tmpdir=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dorg.lwjgl.system.SharedLibraryExtractPath=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dio.netty.native.workdir=D:\MINE2024\curseforge\minecraft\Install\bin\631eecf71e69cf006fcef5c639d1e634321b03f0 -Dminecraft.launcher.brand=minecraft-launcher -Dminecraft.launcher.version=2.27.19 -Djava.net.preferIPv6Addresses=system -DignoreList=bootstraplauncher,securejarhandler,asm-commons,asm-util,asm-analysis,asm-tree,asm,JarJarFileSystems,client-extra,fmlcore,javafmllanguage,lowcodelanguage,mclanguage,forge-,forge-47.2.20.jar,forge-47.2.20 -DmergeModules=jna-5.10.0.jar,jna-platform-5.10.0.jar -DlibraryDirectory=D:\MINE2024\curseforge\minecraft\Install\libraries --module-path=D:\MINE2024\curseforge\minecraft\Install\libraries/cpw/mods/bootstraplauncher/1.1.2/bootstraplauncher-1.1.2.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/cpw/mods/securejarhandler/2.1.10/securejarhandler-2.1.10.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-commons/9.5/asm-commons-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-util/9.5/asm-util-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-analysis/9.5/asm-analysis-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm-tree/9.5/asm-tree-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/org/ow2/asm/asm/9.5/asm-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries/net/minecraftforge/JarJarFileSystems/0.3.19/JarJarFileSystems-0.3.19.jar --add-modules=ALL-MODULE-PATH --add-opens=java.base/java.util.jar=cpw.mods.securejarhandler --add-opens=java.base/java.lang.invoke=cpw.mods.securejarhandler --add-exports=java.base/sun.security.util=cpw.mods.securejarhandler --add-exports=jdk.naming.dns/com.sun.jndi.dns=java.naming -Xmx20096m -Xms256m -Dminecraft.applet.TargetDirectory=D:\MINE2024\curseforge\minecraft\Instances\All the Mods 9 - ATM9 -Dfml.ignorePatchDiscrepancies=true -Dfml.ignoreInvalidMinecraftCertificates=true -Duser.language=en -Duser.country=US -DlibraryDirectory=D:\MINE2024\curseforge\minecraft\Install\libraries -Dlog4j.configurationFile=D:\MINE2024\curseforge\minecraft\Install\assets\log_configs\client-1.12.xml 
java_command: cpw.mods.bootstraplauncher.BootstrapLauncher --username TiozaoDosGames --version forge-47.2.20 --gameDir D:\MINE2024\curseforge\minecraft\Instances\All the Mods 9 - ATM9 --assetsDir D:\MINE2024\curseforge\minecraft\Install\assets --assetIndex 5 --uuid 6057701fee244ab2975baf9dc877ed39 -P_ZTXe3Q-MepsFWVg --clientId NjVjNzUxOGYtMmQ5OS00OWIzLWE0ODEtYWI0YmY3ZTkwNGZk --xuid 2535454040662408 --userType msa --versionType release --width 1024 --height 768 --quickPlayPath D:\MINE2024\curseforge\minecraft\Install\quickPlay\java\1722205879594.json --launchTarget forgeclient --fml.forgeVersion 47.2.20 --fml.mcVersion 1.20.1 --fml.forgeGroup net.minecraftforge --fml.mcpVersion 20230612.114412
java_class_path (initial): D:\MINE2024\curseforge\minecraft\Install\libraries\cpw\mods\securejarhandler\2.1.10\securejarhandler-2.1.10.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\ow2\asm\asm\9.5\asm-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\ow2\asm\asm-commons\9.5\asm-commons-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\ow2\asm\asm-tree\9.5\asm-tree-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\ow2\asm\asm-util\9.5\asm-util-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\ow2\asm\asm-analysis\9.5\asm-analysis-9.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\accesstransformers\8.0.4\accesstransformers-8.0.4.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\antlr\antlr4-runtime\4.9.1\antlr4-runtime-4.9.1.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\eventbus\6.0.5\eventbus-6.0.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\forgespi\7.0.1\forgespi-7.0.1.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\coremods\5.0.1\coremods-5.0.1.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\cpw\mods\modlauncher\10.0.9\modlauncher-10.0.9.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\unsafe\0.2.0\unsafe-0.2.0.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecraftforge\mergetool\1.1.5\mergetool-1.1.5-api.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\com\electronwill\night-config\core\3.6.4\core-3.6.4.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\com\electronwill\night-config\toml\3.6.4\toml-3.6.4.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\org\apache\maven\maven-artifact\3.8.5\maven-artifact-3.8.5.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\jodah\typetools\0.6.3\typetools-0.6.3.jar;D:\MINE2024\curseforge\minecraft\Install\libraries\net\minecrell\terminalconsoleappender\1.2.0\terminalconsole
Launcher Type: SUN_STANDARD

[Global flags]
     intx CICompilerCount                          = 4                                         {product} {ergonomic}
     uint ConcGCThreads                            = 2                                         {product} {ergonomic}
     uint G1ConcRefinementThreads                  = 8                                         {product} {ergonomic}
   size_t G1HeapRegionSize                         = 16777216                                  {product} {ergonomic}
    uintx GCDrainStackTargetSize                   = 64                                        {product} {ergonomic}
    ccstr HeapDumpPath                             = MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump         {manageable} {command line}
   size_t InitialHeapSize                          = 268435456                                 {product} {command line}
   size_t MarkStackSize                            = 4194304                                   {product} {ergonomic}
   size_t MaxHeapSize                              = 21072183296                               {product} {command line}
   size_t MaxNewSize                               = 12633243648                               {product} {ergonomic}
   size_t MinHeapDeltaBytes                        = 16777216                                  {product} {ergonomic}
   size_t MinHeapSize                              = 268435456                                 {product} {command line}
    uintx NonNMethodCodeHeapSize                   = 5839372                                {pd product} {ergonomic}
    uintx NonProfiledCodeHeapSize                  = 122909434                              {pd product} {ergonomic}
    uintx ProfiledCodeHeapSize                     = 122909434                              {pd product} {ergonomic}
    uintx ReservedCodeCacheSize                    = 251658240                              {pd product} {ergonomic}
     bool SegmentedCodeCache                       = true                                      {product} {ergonomic}
   size_t SoftMaxHeapSize                          = 21072183296                            {manageable} {ergonomic}
     intx ThreadStackSize                          = 1024                                   {pd product} {command line}
     bool UseCompressedClassPointers               = true                           {product lp64_product} {ergonomic}
     bool UseCompressedOops                        = true                           {product lp64_product} {ergonomic}
     bool UseG1GC                                  = true                                      {product} {ergonomic}
     bool UseLargePagesIndividualAllocation        = false                                  {pd product} {ergonomic}

Logging:
Log output configuration:
 #0: stdout all=warning uptime,level,tags
 #1: stderr all=off uptime,level,tags

Environment Variables:
PATH=C:\Program Files\Common Files\Oracle\Java\javapath;C:\Python312\Scripts\;C:\Python312\;C:\Program Files (x86)\Common Files\Oracle\Java\java8path;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Program Files\Docker\Docker\resources\bin;C:\Program Files\Go\bin;C:\Program Files\NVIDIA Corporation\NVIDIA NvDLISR;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;\AppData\Local\Microsoft\WindowsApps;\AppData\Local\Programs\Microsoft VS Code\bin;\AppData\Local\GitHubDesktop\bin;\AppData\Roaming\npm;\go\bin
USERNAME=%USERPROFILE%
OS=Windows_NT
PROCESSOR_IDENTIFIER=AMD64 Family 23 Model 24 Stepping 1, AuthenticAMD
TMP=<TMP>
TEMP=<TEMP>



---------------  S Y S T E M  ---------------

OS:
 Windows 10 , 64 bit Build 19041 (10.0.19041.4597)
OS uptime: 6 days 23:00 hours

CPU: total 8 (initial active 8) (8 cores per cpu, 2 threads per core) family 23 model 24 stepping 1 microcode 0x0, cx8, cmov, fxsr, ht, mmx, 3dnowpref, sse, sse2, sse3, ssse3, sse4a, sse4.1, sse4.2, popcnt, lzcnt, tsc, tscinvbit, avx, avx2, aes, clmul, bmi1, bmi2, adx, sha, fma, vzeroupper, clflush, clflushopt
Processor Information for all 8 processors :
  Max Mhz: 3700, Current Mhz: 3700, Mhz Limit: 3700

Memory: 4k page, system-wide physical 32716M (7918M free)
TotalPageFile size 62523M (AvailPageFile size 24M)
current process WorkingSet (physical memory assigned to process): 8414M, peak: 17828M
current process commit charge ("private bytes"): 31484M, peak: 31819M

vm_info: OpenJDK 64-Bit Server VM (17.0.8+7-LTS) for windows-amd64 JRE (17.0.8+7-LTS), built on Jul  7 2023 17:21:55 by "MicrosoftCorporation" with MS VC++ 16.10 / 16.11 (VS2019)

END.
