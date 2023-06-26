#define _GLIBCXX_DEBUG
#include <bits/stdc++.h> // ←許して
using namespace std;
#define decp(n) cout<<fixed<<setprecision((int)n)

double getfv(double v){
    if(v < 5)
    {
        return 3.05 / (3.05 + v);
    }
    else if(v < 20)
    {
        return 6.1 / (6.1 + v);
    }
    else if(v < 50)
    {
        return 5.5 + (5.5 + sqrt(v));
    }
    else
    {
        return 0;
    }
}

double gety(int z){
    if(z < 12)
    {
        return 0;
    }
    else if (z == 12)
    {
        return 0.277;
    }
    else if (z == 13)
    {
        return 0.292;
    }
    else if (z == 14)
    {
        return 0.308;
    }
    else if (z == 15)
    {
        return 0.319;
    }
    else if (z == 16)
    {
        return 0.325;
    }
    else if (z == 17)
    {
        return 0.330;
    }
    else if (z == 18)
    {
        return 0.335;
    }
    else if (z == 19)
    {
        return 0.340;
    }
    else if (z == 20)
    {
        return 0.346;
    }
    else if (z == 24)
    {
        return 0.352;
    }
    else if (z < 26)
    {
        return 0.359;
    }
    else if (z < 28)
    {
        return 0.367;
    }
    else if (z < 30)
    {
        return 0.372;
    }
    else if (z < 34)
    {
        return 0.377;
    }
    else if (z < 38)
    {
        return 0.388;
    }
    else if (z < 43)
    {
        return 0.400;
    }
    else if (z < 50)
    {
        return 0.411;
    }
    else if (z < 60)
    {
        return 0.422;
    }
    else if (z < 75)
    {
        return 0.433;
    }
    else if (z < 100)
    {
        return 0.443;
    }
    else if (z < 150)
    {
        return 0.454;
    }
    else if (z < 300)
    {
        return 0.464;
    }
    else if (z == 300)
    {
        return 0.474;
    }
    else{
        return 0.484;
    }
}

int calc(double m12, double m34){
    // 毎回定数とか用意しててバカみたいだけど書き直すのだるかった。。
    decp(10);
    const double pi = 3.14159265358979323846264338;
    const double g = 9.80665; // m/s^2

    const double fw = 0.74;
    const double sigma0 = 60.0; // MPa
    const double tau0 = 50.0;   // MPa
    const double k = 0.053 * g; // MPa
    const double fb = 3.0;

    double pw = 3700.0; // W
    double n1 = 1500.0; // rpm
    double omega1 = 2.0 * pi * n1 / 60.0; // rad/s

    //int m12 = 11.0; // mm
    //int m34 = 12.0; // mm

    double minrr = 19.9; // Min Reduction Ratio
    double maxrr = 20.1; // Max Reduction Ratio
    double maxd = 400.0; // mm これより直径大きくしないようにする

    //vector<vector<int>> ans(1000, vector<int>(4));
    //int cnt = 0;

    // 実用上の最小歯数は14枚らしい（理論上は17枚らしい）
    for (int z1 = 14; z1 <= 300; z1++){
        for (int z2 = z1; z2 <= 300; z2++){
            if(__gcd(z1, z2) != 1)
            { // 互いに素であること判定
                continue;
            }
            if (((int)(100.0 * m12) * (z1 + z2)) % (int)(100.0 * m34) != 0)
            { // z4 is an integer.
                continue;
            }
            for (int z3 = 14; z3 <= 300; z3++){
                int z4 = (int)(100.0 * m12) * (z1 + z2) / (int)(100.0 * m34) - z3;

                double rr = (double)z2 * (double)z4 / ((double)z1 * (double)z3);
                if(rr < minrr || rr > maxrr)
                { // 減速比の範囲判定
                    continue;
                }

                if(__gcd(z3, z4) != 1)
                { // 互いに素であること判定
                    continue;
                }

                double d1 = z1 * m12; // mm
                double d2 = z2 * m12; // mm
                double d3 = z3 * m34; // mm
                double d4 = z4 * m34; // mm

                if (d1 > maxd || d2 > maxd || d3 > maxd || d4 > maxd)
                { // 直径がでかすぎてもダメ
                    continue;
                }

                double omega2 = omega1 * z1 / z2; // rad/s
                double omega3 = omega2;           // rad/s
                double omega4 = omega3 * z3 / z4; // rad/s

                double v12 = (omega1 * d1 / 2.0) * 1e-3; // m/s m/sに変換しておく
                double v34 = (omega3 * d3 / 2.0) * 1e-3; // m/s m/sに変換しておく

                double f12 = pw / v12; // N
                double f34 = pw / v34; // N

                double fv12 = getfv(v12);
                double sigmab12 = fw * fv12 * sigma0; // MPa
                double b12 = fb * pi * m12;           // mm
                double y1 = gety(z1);
                double y2 = gety(z2);
                double fl1 = sigmab12 * m12 * b12 * y1; // N
                double fl2 = sigmab12 * m12 * b12 * y2; // N
                double fv34 = getfv(v34);
                double sigmab34 = fw * fv34 * sigma0; // MPa
                double b34 = fb * pi * m34;           // mm
                double y3 = gety(z3);
                double y4 = gety(z4);
                double fl3 = sigmab34 * m34 * b34 * y3; // N
                double fl4 = sigmab34 * m34 * b34 * y4; // N

                double fh12 = fv12 * k * d1 * b12 * 2.0 * z2 / (z1 + z2); // N
                double fh34 = fv34 * k * d3 * b34 * 2.0 * z4 / (z3 + z4); // N

                double t4 = f34 * d4 / 2000.0; // Nm
                double tmp = 28.0 / 1000.0; // m  入力軸及び出力軸の半径
                double tau = 16.0 * t4 / (pi * tmp * tmp * tmp) * 1e-6; // MPa
                double r = tau / tau0; // safety ratio

                if(f12 < min(fl1, fl2) && f34 < min(fl3, fl4) && f12 < fh12 && f34 < fh34)
                { // 応力とかの条件判定
                    cout << "m12 : " << m12 << ", m34 : " << m34 << endl;
                    cout << "z1 : " << z1 << ", z2 : " << z2 << ", z3 : " << z3 << ", z4 : " << z4 << endl;
                    cout << "Reduction Ratio : " << rr << endl;
                    cout << "d1 : " << d1 << ", d2 : " << d2 << ", d3 : " << d3 << ", d4 : " << d4 << endl;
                    cout << "omega1 : " << omega1 << ", omega2 : " << omega2 << ", omega3 : " << omega3 << ", omega4 : " << omega4 << endl;
                    cout << "v12 : " << v12 << ", v34 : " << v34 << endl;
                    cout << "f12 : " << f12 << ", f34 : " << f34 << endl;
                    cout << "fl1 : " << fl1 << ", fl2 : " << fl2 << ", fl3 : " << fl3 << ", fl4 : " << fl4 << endl;
                    cout << "fh12 : " << fh12 << ", fh34 : " << fh34 << endl;
                    cout << "T4 : " << t4 << endl;
                    cout << "tau : " << tau << endl;
                    cout << "Safety Ratio : " << r << endl;
                    cout << "b12 : " << b12 << ", b34 : " << b34 << endl;
                    cout << "y1 : " << y1 << ", y2 : " << y2 << ", y3 : " << y3 << ", y4 : " << y4 << endl;
                    cout << "======================================================================================================" << endl;
                }
            }
        }
    }
    return 0;
}

int main(void){
    vector<double> m(25); // mm
    m[0] = 0.1;
    m[1] = 0.15;
    m[2] = 0.2;
    m[3] = 0.25;
    m[4] = 0.3;
    m[5] = 0.4;
    m[6] = 0.5;
    m[7] = 0.6;
    m[8] = 0.8;
    m[9] = 1.0;
    m[10] = 1.25;
    m[11] = 1.5;
    m[12] = 2.0;
    m[13] = 2.5;
    m[14] = 3.0;
    m[15] = 4.0;
    m[16] = 5.0;
    m[17] = 6.0;
    m[18] = 8.0;
    m[19] = 10.0;
    m[20] = 12.0;
    m[21] = 16.0;
    m[22] = 20.0;
    m[23] = 22.0;
    m[24] = 25.0;

    for (int i = 0; i < 25; i++){
        for (int j = i; j < 25; j++){ // mの任意の組み合わせ 計算量減らすためにi<=jとする
            calc(m[i], m[j]);
        }
    }

    cout << endl << "test.exe > ../ut_lecture/534aerospace_basic_design/4/memo.txt" << endl;
}
