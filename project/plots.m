M = linspace(0.01,5);

Rwd = 6.2e3*(M.^(-1/3));
Rns = 1.2e4*(M.^(-1/3));
Rbh = 2.95*M;
Rsu = 2.4e5*(M.^(1/3));

loglog(M,Rwd)
hold on
loglog(M,Rns)
hold on
loglog(M,Rbh)
hold on
loglog(M,Rsu)
title('Log R/km as a Function of Log M/Msun')
xlabel('M/Msun')
ylabel('R/km')
ylim([0.01,1000000])
legend('White Dwarf','Neutron Star', 'Blackhole', 'Sun', 'location', 'southeast')
