# GIS 数据展示平台（全栈）

基于 FastAPI + PostgreSQL/PostGIS + Docker + OpenLayers/Leaflet 的全栈 GIS 项目。

## 技术栈

- **后端**：FastAPI + SQLAlchemy + GeoAlchemy2
- **数据库**：PostgreSQL 16 + PostGIS 3.4
- **容器化**：Docker + Docker Compose
- **前端**：Leaflet + OpenLayers（双引擎可切换）

## 功能

- POI（兴趣点）增删查，支持 GeoJSON 格式输出
- 区域（Region）空间数据管理
- Leaflet / OpenLayers 双地图引擎一键切换
- 前端面板直接添加 POI
- 预置广州 8 个示例 POI

## 快速启动

`ash
# 1. 启动全部服务（数据库 + API）
docker-compose up -d

# 2. 打开前端页面
# 直接用浏览器打开 frontend/index.html
# 或通过任意静态服务器托管
`

## 项目结构

`
gis-platform/
├── backend/
│   ├── main.py          # FastAPI 入口 + 路由
│   ├── models.py         # SQLAlchemy + PostGIS 模型
│   ├── schemas.py        # Pydantic 请求/响应模型
│   ├── database.py       # 数据库连接配置
│   └── requirements.txt
├── frontend/
│   └── index.html        # 双引擎地图前端
├── data/
│   └── init.sql          # 数据库初始化 + 示例数据
├── Dockerfile
├── docker-compose.yml
└── README.md
`

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/health | 健康检查 |
| GET | /api/pois | 获取所有 POI |
| GET | /api/pois/geojson | 获取 POI GeoJSON |
| POST | /api/pois | 新增 POI |
| DELETE | /api/pois/{id} | 删除 POI |
| GET | /api/regions/geojson | 获取区域 GeoJSON |
| POST | /api/regions | 新增区域 |