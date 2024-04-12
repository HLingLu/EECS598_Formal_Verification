close all; clear
cpu_time_ori = [0.195733, 0.212261, 0.184344, 0.185284, 0.19741, 0.228534, 0.288753, 0.203887, 0.240093, 0.248326];
cpu_time_sym = [0.165506, 0.183646, 0.205721, 0.230071, 0.220151, 0.224011, 0.272287, 0.337334, 0.240977, 0.290774];
num_res_ori = [462, 505, 365, 424, 380, 485, 529, 481, 346, 298];
num_res_sym = [406, 505, 312, 447, 427, 495, 345, 421, 330, 458];
num_conf_ori = [9075, 9611, 9648, 9814, 10284, 12231, 13076, 10805, 12557, 12090];
num_conf_sym = [8685, 8392, 9099, 10509, 11862, 10773, 14416, 15066, 9257, 14066];
num_dec_ori = [21590, 23065, 23053, 23038, 25131, 28516, 31583, 28484, 30019, 27294];
num_dec_sym = [20060, 22310, 20083, 26979, 27101, 28902, 32718, 33002, 25299, 33544];
num_pro_ori = [1671780, 1703493, 1334422, 1399131, 1499762, 1585604, 2166873, 1554428, 1696294, 1951766];
num_pro_sym = [1231079, 1378892, 1536123, 1709530, 1557884, 1613495, 1810704, 2401611, 1843874, 1949260];


%% Plot cpu time
min_time = min(min(cpu_time_ori), min(cpu_time_sym));
max_time = max(max(cpu_time_ori), max(cpu_time_sym));

figure(1)
plot([min_time max_time], [min_time max_time],'LineWidth',2)
hold on
plot(cpu_time_ori, cpu_time_sym,'o','LineWidth',2)
title('CPU time to solve the instance')
xlabel('Statistic for original formula')
ylabel('Statistic for SBP-augmented formula')
saveas(gcf,'Figures/CPU.png')

%% Plot number of restarts
min_res = min(min(num_res_ori), min(num_res_sym));
max_res = max(max(num_res_ori), max(num_res_sym));

figure(2)
plot([min_res max_res], [min_res max_res],'LineWidth',2)
hold on
plot(num_res_ori, num_res_sym,'o','LineWidth',2)
title('Number of restarts')
xlabel('Statistic for original formula')
ylabel('Statistic for SBP-augmented formula')
saveas(gcf,'Figures/restarts.png')

%% Plot number of conflicts
min_conf = min(min(num_conf_ori), min(num_conf_sym));
max_conf = max(max(num_conf_ori), max(num_conf_sym));

figure(3)
plot([min_conf max_conf], [min_conf max_conf],'LineWidth',2)
hold on
plot(num_conf_ori, num_conf_sym,'o','LineWidth',2)
title('Number of conflicts')
xlabel('Statistic for original formula')
ylabel('Statistic for SBP-augmented formula')
saveas(gcf,'Figures/conflicts.png')

%% Plot number of decisions
min_dec = min(min(num_dec_ori), min(num_dec_sym));
max_dec = max(max(num_dec_ori), max(num_dec_sym));

figure(4)
plot([min_dec max_dec], [min_dec max_dec],'LineWidth',2)
hold on
plot(num_dec_ori, num_dec_sym,'o','LineWidth',2)
title('Number of decisions')
xlabel('Statistic for original formula')
ylabel('Statistic for SBP-augmented formula')
saveas(gcf,'Figures/decisions.png')

%% Plot number of propagations
min_pro = min(min(num_pro_ori), min(num_pro_sym));
max_pro = max(max(num_pro_ori), max(num_pro_sym));

figure(5)
plot([min_pro max_pro], [min_pro max_pro],'LineWidth',2)
hold on
plot(num_pro_ori, num_pro_sym,'o','LineWidth',2)
title('Number of propagations')
xlabel('Statistic for original formula')
ylabel('Statistic for SBP-augmented formula')
saveas(gcf,'Figures/propagations.png')
