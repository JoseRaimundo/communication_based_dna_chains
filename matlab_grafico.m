z = csvread ("data.csv");

[X,Y] = meshgrid(1:columns(z),1:rows(z));
Z = z;
C = z;
direction = [0 0 1];
rotate(surf(X,Y,C,Z),direction,180)

colorbar