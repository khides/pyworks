# encoding: utf-8
# newline code: LF
# lang: python3.9.5
"""
東京大学工学部航空宇宙工学科 岡本岳
2021/1/15 作成
宇宙軌道力学 第1回レポート

* ディレクトリ（ファイル）構造
-images
  - *.jpg
- calc01.py

* 単位
  - km
  - s
  - rad

* ベクトルは末尾_をつけて表す
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import ScalarFormatter
from tabulate import tabulate

mpl.rcParams["agg.path.chunksize"] = 10000


class SpaceOrbit:
    def __init__(self, num_of_div_t_plot=20, eps=1e-6, num_of_div_runge_kutta=int(1e5)):
        self.mu = 3.986 * 1e5
        self.R = 6371

        self.r0_ = np.array([6000 + self.R, 0, 0], dtype=np.float64)
        self.v0_ = np.array([3, 4, 5], dtype=np.float64)
        self.num_of_div_t_plot = num_of_div_t_plot

        self.eps = eps
        self.num_of_div_runge_kutta = num_of_div_runge_kutta

        # sns.set_style("darkgrid")

    def table_print(self, headers, contents):
        table = tabulate(contents, headers, tablefmt='grid')
        print(table)

    def draw_2d(self, x, y, x_scatter, y_scatter, label, label_loc, xlabel, ylabel, title, file_name, color=np.array([False])):
        fig = plt.figure(figsize=(12, 8), facecolor="w", linewidth=0, edgecolor="w", tight_layout=True)
        ax = fig.add_subplot(111, aspect="equal")
        plt.rcParams['font.size'] = 18
        cmap = plt.get_cmap("tab10")

        if len(x_scatter) > 0:
            for i in range(len(x_scatter)):
                ax.scatter(x_scatter[i], y_scatter[i], marker=".", s=120, c="red", linestyle="None", alpha=1.0, zorder=3)
                ax.text(x_scatter[i]+500, y_scatter[i], f"$t=${i}", ha="left", va="center", rotation=0, size=16, color="black")

        if y.ndim == 1 and type(y[0]) is not list and type(y[0]) is not np.ndarray:
            if not color[0]:
                color[0] = "b-"

            if label == "":
                ax.plot(x, y, c=color[0], ls="-", lw=2)
            else:
                ax.plot(x, y, c=color[0], ls="-", lw=2, label=label)
                ax.legend(loc=label_loc, fontsize=18, shadow=True, facecolor="w")
        else:
            if x.ndim == 1 and type(x[0]) is not list and type(x[0]) is not np.ndarray:
                if label == "":
                    for i in range(len(y)):
                        if not color[i]:
                            ax.plot(x, y[i], c=cmap(i), ls="-", lw=1)
                        else:
                            ax.plot(x, y[i], c=color[i], ls="-", lw=1)
                else:
                    for i in range(len(y)):
                        if not color[i]:
                            ax.plot(x, y[i], c=cmap(i), ls="-", lw=1, label=label[i])
                        else:
                            ax.plot(x, y[i], c=color[i], ls="-", lw=1, label=label[i])
                    ax.legend(loc=label_loc, fontsize=18, shadow=True, facecolor="w")
            else:
                if label == "":
                    for i in range(len(y)):
                        if not color[i]:
                            ax.plot(x[i], y[i], c=cmap(i), ls="-", lw=1)
                        else:
                            ax.plot(x[i], y[i], c=color[i], ls="-", lw=1)
                else:
                    for i in range(len(y)):
                        if not color[i]:
                            ax.plot(x[i], y[i], c=cmap(i), ls="-", lw=1, label=label[i])
                        else:
                            ax.plot(x[i], y[i], c=color[i], ls="-", lw=1, label=label[i])
                    ax.legend(loc=label_loc, fontsize=18, shadow=True, facecolor="w")
        # ax.set_xlim([0.95 * max(x), 1.05 * max(x)])
        # ax.set_ylim([0.95 * max(y), 1.05 * max(y)])

        # オフセット
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.xaxis.offsetText.set_fontsize(20)
        ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.yaxis.offsetText.set_fontsize(20)
        ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)

        ax.set_xlabel(xlabel, fontsize=20)
        ax.set_ylabel(ylabel, fontsize=20)
        ax.set_title(title, fontsize=26)
        ax.grid(color="gainsboro")
        plt.savefig(f'images/{file_name}.jpg')
        plt.show()

    def draw_3d(self, x, y, z, x_scatter, y_scatter, z_scatter, label_loc, xlabel, ylabel, zlabel, title, file_name):
        fig = plt.figure(figsize=(12, 8), facecolor="w", linewidth=0, edgecolor="w", tight_layout=True)
        ax = fig.add_subplot(projection="3d")
        ax.set_box_aspect([1, 1, 1])
        plt.rcParams['font.size'] = 18

        # earth
        theta, phi = np.mgrid[0: 2*np.pi: 500j, 0: 2*np.pi: 500j]
        x_earth = self.R * np.cos(theta) * np.sin(phi)
        y_earth = self.R * np.sin(theta) * np.sin(phi)
        z_earth = self.R * np.cos(phi)
        ax.plot_wireframe(x_earth, y_earth, z_earth, color="dodgerblue", linestyle="-", linewidth=0.5, label="earth")

        # spacecraft
        if len(x_scatter) > 0:
            for i in range(len(x_scatter)):
                ax.scatter(x_scatter[i], y_scatter[i], z_scatter[i], marker=".", s=50, c="red", linestyle="None", alpha=1.0)
                ax.text(x_scatter[i]+500, y_scatter[i], z_scatter[i], f"$t=${i}", ha="left", va="center", rotation=0, size=14, color="black")
        ax.plot(x, y, z, c="black", ls="-", lw=1, label="spacecraft")

        # 目盛りの設定
        x_max = max(max(x_earth.flatten()), max(x))
        x_min = min(min(x_earth.flatten()), min(x))
        y_max = max(max(y_earth.flatten()), max(y))
        y_min = min(min(y_earth.flatten()), min(y))
        z_max = max(max(z_earth.flatten()), max(z))
        z_min = min(min(z_earth.flatten()), min(z))
        x_mid = (x_max + x_min) * 0.5
        y_mid = (y_max + y_min) * 0.5
        z_mid = (z_max + z_min) * 0.5
        range_max = max(x_max - x_mid, y_max - y_mid, z_max - z_mid) * 1.05
        ax.set_xlim3d([x_mid - range_max, x_mid + range_max])
        ax.set_ylim3d([y_mid - range_max, y_mid + range_max])
        ax.set_zlim3d([z_mid - range_max, z_mid + range_max])

        # オフセット
        ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
        ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
        ax.zaxis.set_major_formatter(ScalarFormatter(useMathText=True))
        ax.ticklabel_format(style="sci", axis="z", scilimits=(0, 0))

        # plt.xticks(fontsize=20)
        # plt.yticks(fontsize=20)
        # plt.zticks(fontsize=20)

        ax.legend(loc=label_loc, fontsize=18, shadow=True, facecolor="w")
        ax.set_xlabel(xlabel, labelpad=10)
        ax.set_ylabel(ylabel, labelpad=8)
        ax.set_zlabel(zlabel, labelpad=6)
        ax.set_title(title, fontsize=26)
        # ax.grid(color="gainsboro")
        ax.view_init(elev=20, azim=-35)
        plt.savefig(f'images/{file_name}.jpg')
        plt.show()

    def newton_raphson(self, t_plot, a, t_p, e):
        def f(E):
            return E - e * np.sin(E) - np.sqrt(self.mu / a**3) * (t_plot - t_p)

        E = np.sqrt(self.mu / a**3) * (t_plot - t_p)
        while 1 - e * np.cos(E) < self.eps:
            E -= f(E) / (1 - e * np.cos(E))

        return E

    def runge_kutta(self, T):
        def f(y_):
            r_ = y_[0]
            v_ = y_[1]
            r = np.sqrt(np.dot(r_, r_))
            return np.array([v_, -self.mu * r_ / r**3])

        y_ = [np.array([self.r0_, self.v0_])]
        delta_t = T / self.num_of_div_runge_kutta
        for _ in range(self.num_of_div_runge_kutta):
            k1_ = f(y_[-1])
            k2_ = f(y_[-1] + np.dot(np.array([[0.5 * delta_t, 0], [0, 0.5 * delta_t]], dtype=np.float64), k1_))
            k3_ = f(y_[-1] + np.dot(np.array([[0.5 * delta_t, 0], [0, 0.5 * delta_t]], dtype=np.float64), k2_))
            k4_ = f(y_[-1] + np.dot(np.array([[delta_t, 0], [0, delta_t]], dtype=np.float64), k3_))

            y_next_ = y_[-1] + np.dot(np.array([[delta_t / 6, 0], [0, delta_t / 6]]), k1_ + 2 * k2_ + 2 * k3_ + k4_)
            y_.append(y_next_)

        return y_

    def main(self):
        # ==================== 1 ==============================
        # 1-1
        h_ = np.cross(self.r0_, self.v0_)
        h = np.sqrt(np.dot(h_, h_))

        # 1-2
        r0 = np.sqrt(np.dot(self.r0_, self.r0_))
        epsilon = np.dot(self.v0_, self.v0_) / 2 - self.mu / r0

        # 1-3
        P_ = np.cross(self.v0_, h_) - self.mu * self.r0_ / r0
        P = np.sqrt(np.dot(P_, P_))

        # 1-4
        p = h**2 / self.mu
        e = P / self.mu

        # 1-5
        a = p / (1 - e**2)
        b = a * np.sqrt(1 - e**2)

        # 1-6
        r_p = a * (1 - e)
        r_a = a * (1 + e)
        v_p = np.sqrt((self.mu / r_p) * (2 * r_a / (r_a + r_p)))
        v_a = np.sqrt((self.mu / r_a) * (2 * r_p / (r_a + r_p)))

        # 1-7
        nu = np.linspace(0, 2*np.pi, int(1e5))
        r = p / (1 + e * np.cos(nu))
        x_orbit_pq = [r[i] * np.cos(nu[i]) for i in range(len(nu))]
        y_orbit_pq = [r[i] * np.sin(nu[i]) for i in range(len(nu))]
        x_earth = self.R * np.cos(nu)
        y_earth = self.R * np.sin(nu)

        self.draw_2d(x=np.array([x_orbit_pq, x_earth]), y=np.array([y_orbit_pq, y_earth]), x_scatter=[], y_scatter=[], label=["spacecraft", "earth"],
                     label_loc="upper left", xlabel="$P$ [km]", ylabel="$Q$ [km]", title="Ellipse Plot (P-Q frame)", file_name="1_6", color=["black", "dodgerblue"])

        # 1-8
        r_pq_ = np.array([x_orbit_pq, y_orbit_pq, [0] * len(nu)])

        P_hat_ = P_ / P
        W_hat_ = h_ / h
        Q_hat_ = np.cross(W_hat_, P_hat_)

        r_xyz_ = np.dot(np.linalg.inv(np.array([P_hat_, Q_hat_, W_hat_])), r_pq_)

        self.draw_3d(x=r_xyz_[0], y=r_xyz_[1], z=r_xyz_[2], x_scatter=[], y_scatter=[], z_scatter=[], label_loc="upper left",
                     xlabel="$X$ [km]", ylabel="$Y$ [km]", zlabel="$Z$ [km]", title="Ellipse Plot (XYZ frame)", file_name="1_7")
        self.draw_2d(x=np.array([r_xyz_[0], x_earth]), y=np.array([r_xyz_[1], y_earth]), x_scatter=[], y_scatter=[], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Y$ [km]", title="Ellipse Plot (X-Y frame)", file_name="1_7_Y", color=["black", "dodgerblue"])
        self.draw_2d(x=np.array([r_xyz_[0], x_earth]), y=np.array([r_xyz_[2], y_earth]), x_scatter=[], y_scatter=[], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Z$ [km]", title="Ellipse Plot (X-Z frame)", file_name="1_7_Z", color=["black", "dodgerblue"])

        print("==================== 1 ==============================")
        self.table_print(
            ["h_", "epsilon", "P_", "p", "e", "a", "b", "r_p", "r_a", "v_p", "v_a"],
            [[h_, epsilon, P_, p, e, a, b, r_p, r_a, v_p, v_a]]
        )

        # ==================== 2 ==============================
        # 2-1
        T = 2 * np.pi * np.sqrt(a**3 / self.mu)

        # 2-2
        nu0 = np.arccos((p / r0 - 1) / e)
        judge = np.cross(self.r0_, P_)[2]  # r0がラプラスベクトルP_より進んでいるかどうか判断
        print("r_0 × P_=", np.cross(self.r0_, P_))
        # np.arccos: retrun [0, 2 * np.pi]
        if judge < 0:
            # r0の方が進んでいる
            if nu0 > np.pi:
                nu0 = 2 * np.pi - nu0
        else:  # 0の場合は省略
            # r0の方が遅れている
            if nu0 < np.pi:
                nu0 - 2 * np.pi - nu0
        E0 = np.arccos((e + np.cos(nu0) / (1 + e * np.cos(nu0))))
        if (nu0 - np.pi) * (E0 - np.pi) < 0:  # nu0と同じ方向
            E0 = 2 * np.pi - E0

        # 2-3
        t_p = -a**2 * np.sqrt(1 - e**2) / h * (E0 - e * np.sin(E0))

        # 2-4
        t_plot = np.linspace(0, T, self.num_of_div_t_plot+1)
        E = [0] * self.num_of_div_t_plot
        E[0] = E0
        for i in range(1, self.num_of_div_t_plot):
            E[i] = self.newton_raphson(t_plot[i], a, t_p, e)

        # 2-5
        r = [a * (1 - e * np.cos(E_)) for E_ in E]  # 1-7で用いたrと変数名被ってることに注意
        nu = [0] * len(E)  # 1-7で用いたnuと変数名被ってることに注意
        for i in range(len(E)):
            nu[i] = np.arccos((np.cos(E[i]) - e) / (1 - e * np.cos(E[i])))
            if np.floor(E[i] / np.pi) % 2 != np.floor(nu[i] / np.pi):  # nuはEと同じ方向
                nu[i] = 2 * np.pi - nu[i]
        x_scatter_pq = [r[i] * np.cos(nu[i]) for i in range(len(r))]
        y_scatter_pq = [r[i] * np.sin(nu[i]) for i in range(len(r))]

        self.draw_2d(x=np.array([x_orbit_pq, x_earth]), y=np.array([y_orbit_pq, y_earth]), x_scatter=x_scatter_pq, y_scatter=y_scatter_pq, label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$P$ [km]", ylabel="$Q$ [km]", title="Ellipse Plot (P-Q frame)", file_name="2_5", color=["black", "dodgerblue"])

        # 2-6
        scatter_pq_ = np.array([x_scatter_pq, y_scatter_pq, [0] * len(x_scatter_pq)])
        scatter_xyz_ = np.dot(np.linalg.inv(np.array([P_hat_, Q_hat_, W_hat_])), scatter_pq_)

        self.draw_3d(x=r_xyz_[0], y=r_xyz_[1], z=r_xyz_[2], x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[1], z_scatter=scatter_xyz_[2], label_loc="upper left",
                     xlabel="$X$ [km]", ylabel="$Y$ [km]", zlabel="$Z$ [km]", title="Ellipse Plot (XYZ frame)", file_name="2_6")
        self.draw_2d(x=np.array([r_xyz_[0], x_earth], dtype=object), y=np.array([r_xyz_[1], y_earth], dtype=object), x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[1], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Y$ [km]", title="Ellipse Plot (X-Y frame)", file_name="2_6_Y", color=["black", "dodgerblue"])
        self.draw_2d(x=np.array([r_xyz_[0], x_earth], dtype=object), y=np.array([r_xyz_[2], y_earth], dtype=object), x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[2], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Z$ [km]", title="Ellipse Plot (X-Z frame)", file_name="2_6_Z", color=["black", "dodgerblue"])

        print("==================== 2 ==============================")
        self.table_print(
            ["T", "nu0", "E0", "t_p"],
            [[T, nu0, E0, t_p]]
        )
        self.table_print([i for i in range(self.num_of_div_t_plot)], [t_plot[:-1], E])

        # ==================== 3 ==============================
        # 3-1
        y_ = self.runge_kutta(T)
        r_xyz_ = np.array([y_[i][0].tolist() for i in range(len(y_))]).T

        self.draw_3d(x=r_xyz_[0], y=r_xyz_[1], z=r_xyz_[2], x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[1], z_scatter=scatter_xyz_[2], label_loc="upper left",
                     xlabel="$X$ [km]", ylabel="$Y$ [km]", zlabel="$Z$ [km]", title="Ellipse Plot (XYZ frame)", file_name="3_1")
        self.draw_2d(x=np.array([r_xyz_[0], x_earth], dtype=object), y=np.array([r_xyz_[1], y_earth], dtype=object), x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[1], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Y$ [km]", title="Ellipse Plot (X-Y frame)", file_name="3_1_Y", color=["black", "dodgerblue"])
        self.draw_2d(x=np.array([r_xyz_[0], x_earth], dtype=object), y=np.array([r_xyz_[2], y_earth], dtype=object), x_scatter=scatter_xyz_[0], y_scatter=scatter_xyz_[2], label=[
                     "spacecraft", "earth"], label_loc="upper left", xlabel="$X$ [km]", ylabel="$Z$ [km]", title="Ellipse Plot (X-Z frame)", file_name="3_1_Z", color=["black", "dodgerblue"])

        error = [1e8] * self.num_of_div_t_plot
        for i in range(len(r_xyz_[0])):
            for j in range(self.num_of_div_t_plot):
                error[j] = min(error[j], np.sqrt((r_xyz_[0][i] - scatter_xyz_[0][j])**2 + (r_xyz_[1][i] - scatter_xyz_[1][j])**2 + (r_xyz_[2][i] - scatter_xyz_[2][j])**2))
        error_ave = np.average(error)

        print("==================== 3 ==============================")
        self.table_print([i for i in range(self.num_of_div_t_plot)], [error])
        print("average of error:", error_ave)
        print("error_ave / R:", error_ave / self.R)

if __name__ == "__main__":
    spaceOrbit = SpaceOrbit(num_of_div_t_plot=20, eps=1e-6, num_of_div_runge_kutta=int(1e5))
    spaceOrbit.main()
