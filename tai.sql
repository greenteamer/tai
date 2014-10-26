/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50614
 Source Host           : localhost
 Source Database       : shop

 Target Server Type    : MySQL
 Target Server Version : 50614
 File Encoding         : utf-8

 Date: 10/26/2014 22:35:40 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `accounts_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `accounts_userprofile`;
CREATE TABLE `accounts_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `shipping_name` varchar(50) NOT NULL,
  `shipping_address_1` varchar(50) NOT NULL,
  `shipping_address_2` varchar(50) NOT NULL,
  `shipping_city` varchar(50) NOT NULL,
  `shipping_country` varchar(50) NOT NULL,
  `shipping_zip` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_81d7010f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `accounts_userprofile`
-- ----------------------------
BEGIN;
INSERT INTO `accounts_userprofile` VALUES ('1', 'teamer777@icloud.com', '79264629960', 'Александр', 'Ул.  Ленина ', 'Ул. Ленина', 'Северск', 'Россия', '636070', '1'), ('2', 'greenteamer@bk.ru', '8-913-8886899', 'asdfad', 'Ул. Ленина', 'Ул. Ленина', 'Северск', 'Россия', '636070', '2');
COMMIT;

-- ----------------------------
--  Table structure for `admin_tools_dashboard_preferences`
-- ----------------------------
DROP TABLE IF EXISTS `admin_tools_dashboard_preferences`;
CREATE TABLE `admin_tools_dashboard_preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `data` longtext NOT NULL,
  `dashboard_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_tools_dashboard_prefer_dashboard_id_374bce90a8a4eefc_uniq` (`dashboard_id`,`user_id`),
  KEY `admin_tools_dashboard_preferences_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_2faedda1f8487376` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `admin_tools_dashboard_preferences`
-- ----------------------------
BEGIN;
INSERT INTO `admin_tools_dashboard_preferences` VALUES ('1', '1', '{\"positions\":{},\"columns\":{},\"disabled\":{\"module_5\":true},\"collapsed\":{\"module_2\":false,\"module_3\":true}}', 'dashboard'), ('2', '1', '{}', 'slider-dashboard');
COMMIT;

-- ----------------------------
--  Table structure for `admin_tools_menu_bookmark`
-- ----------------------------
DROP TABLE IF EXISTS `admin_tools_menu_bookmark`;
CREATE TABLE `admin_tools_menu_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_tools_menu_bookmark_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_6af2836063b2844f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add permission', '1', 'add_permission'), ('2', 'Can change permission', '1', 'change_permission'), ('3', 'Can delete permission', '1', 'delete_permission'), ('4', 'Can add group', '2', 'add_group'), ('5', 'Can change group', '2', 'change_group'), ('6', 'Can delete group', '2', 'delete_group'), ('7', 'Can add user', '3', 'add_user'), ('8', 'Can change user', '3', 'change_user'), ('9', 'Can delete user', '3', 'delete_user'), ('10', 'Can add content type', '4', 'add_contenttype'), ('11', 'Can change content type', '4', 'change_contenttype'), ('12', 'Can delete content type', '4', 'delete_contenttype'), ('13', 'Can add session', '5', 'add_session'), ('14', 'Can change session', '5', 'change_session'), ('15', 'Can delete session', '5', 'delete_session'), ('16', 'Can add site', '6', 'add_site'), ('17', 'Can change site', '6', 'change_site'), ('18', 'Can delete site', '6', 'delete_site'), ('19', 'Can add flat page', '7', 'add_flatpage'), ('20', 'Can change flat page', '7', 'change_flatpage'), ('21', 'Can delete flat page', '7', 'delete_flatpage'), ('22', 'Can add log entry', '8', 'add_logentry'), ('23', 'Can change log entry', '8', 'change_logentry'), ('24', 'Can delete log entry', '8', 'delete_logentry'), ('25', 'Can add migration history', '9', 'add_migrationhistory'), ('26', 'Can change migration history', '9', 'change_migrationhistory'), ('27', 'Can delete migration history', '9', 'delete_migrationhistory'), ('28', 'Can add category', '10', 'add_category'), ('29', 'Can change category', '10', 'change_category'), ('30', 'Can delete category', '10', 'delete_category'), ('31', 'Can add product', '11', 'add_product'), ('32', 'Can change product', '11', 'change_product'), ('33', 'Can delete product', '11', 'delete_product'), ('34', 'Can add product image', '12', 'add_productimage'), ('35', 'Can change product image', '12', 'change_productimage'), ('36', 'Can delete product image', '12', 'delete_productimage'), ('37', 'Can add characteristic type', '13', 'add_characteristictype'), ('38', 'Can change characteristic type', '13', 'change_characteristictype'), ('39', 'Can delete characteristic type', '13', 'delete_characteristictype'), ('40', 'Can add characteristic', '14', 'add_characteristic'), ('41', 'Can change characteristic', '14', 'change_characteristic'), ('42', 'Can delete characteristic', '14', 'delete_characteristic'), ('43', 'Can add cart item', '15', 'add_cartitem'), ('44', 'Can change cart item', '15', 'change_cartitem'), ('45', 'Can delete cart item', '15', 'delete_cartitem'), ('46', 'Can add user profile', '16', 'add_userprofile'), ('47', 'Can change user profile', '16', 'change_userprofile'), ('48', 'Can delete user profile', '16', 'delete_userprofile'), ('49', 'Can add order', '17', 'add_order'), ('50', 'Can change order', '17', 'change_order'), ('51', 'Can delete order', '17', 'delete_order'), ('52', 'Can add order item', '18', 'add_orderitem'), ('53', 'Can change order item', '18', 'change_orderitem'), ('54', 'Can delete order item', '18', 'delete_orderitem'), ('55', 'Can add Post', '19', 'add_news'), ('56', 'Can change Post', '19', 'change_news'), ('57', 'Can delete Post', '19', 'delete_news'), ('58', 'Can add search term', '20', 'add_searchterm'), ('59', 'Can change search term', '20', 'change_searchterm'), ('60', 'Can delete search term', '20', 'delete_searchterm'), ('61', 'Can add kv store', '21', 'add_kvstore'), ('62', 'Can change kv store', '21', 'change_kvstore'), ('63', 'Can delete kv store', '21', 'delete_kvstore'), ('64', 'Can add order one click', '22', 'add_orderoneclick'), ('65', 'Can change order one click', '22', 'change_orderoneclick'), ('66', 'Can delete order one click', '22', 'delete_orderoneclick'), ('67', 'Can add dashboard preferences', '23', 'add_dashboardpreferences'), ('68', 'Can change dashboard preferences', '23', 'change_dashboardpreferences'), ('69', 'Can delete dashboard preferences', '23', 'delete_dashboardpreferences'), ('70', 'Can add bookmark', '24', 'add_bookmark'), ('71', 'Can change bookmark', '24', 'change_bookmark'), ('72', 'Can delete bookmark', '24', 'delete_bookmark'), ('73', 'Can add slider', '25', 'add_slider'), ('74', 'Can change slider', '25', 'change_slider'), ('75', 'Can delete slider', '25', 'delete_slider');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `auth_user`
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES ('1', 'admin', '', '', 'sdfs@sdf.ru', 'pbkdf2_sha256$10000$zLEFXnsPDqmJ$cJxS+82DNOj0AcCbPvA1VhxBMdUVreLBh/wKX89Bc4Q=', '1', '1', '1', '2014-04-28 20:48:44', '2014-01-03 22:51:07'), ('2', 'user', '', '', '', 'pbkdf2_sha256$10000$tCgQNxRJXKW0$+OO5DIk+NMfkhJXPDSC/TvV3X2n92O2GP8dP5ZiCWjA=', '0', '1', '0', '2014-01-04 00:21:11', '2014-01-04 00:21:10');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `cart_items`
-- ----------------------------
DROP TABLE IF EXISTS `cart_items`;
CREATE TABLE `cart_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_id` varchar(50) NOT NULL,
  `date_added` datetime NOT NULL,
  `quantity` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_items_bb420c12` (`product_id`),
  CONSTRAINT `product_id_refs_id_764428ba` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `cart_items`
-- ----------------------------
BEGIN;
INSERT INTO `cart_items` VALUES ('58', 'QjW6lxXQYRl73Nnn4uIg7xNniHVx3hhs$TZ7s0ALcglI1MynjQ', '2014-04-20 02:39:44', '1', '11'), ('59', 'M5QR&3Rw8%6y0%#n48aRRq42uRYm(JE)v!y7n!EDOQ3fmXI1i^', '2014-04-22 20:24:39', '1', '11'), ('65', 'sQQ4X)TI9Ssh9sSGdWdBE#LYC^g8d2lMZztz4106hL00h1eBA(', '2014-04-24 00:04:14', '1', '12'), ('67', 'fIUd$T930$SP4lD4Qs%1*dWg1^5raGCy11zXRXQYV2yXa$5Omi', '2014-04-24 02:20:14', '1', '11'), ('68', 'fIUd$T930$SP4lD4Qs%1*dWg1^5raGCy11zXRXQYV2yXa$5Omi', '2014-04-24 02:51:20', '1', '13'), ('69', 'qQ(J!$GzzAFWui*QFe&juxDtvh0ciqztb$KWF4w2ZZz32Wgu#N', '2014-04-26 02:22:32', '1', '12'), ('81', 'jHhg)XKC9udR47Ew9@q2vof)Zx(obz)L@a8nEvZza$eYXbLy!F', '2014-04-28 20:19:18', '1', '11'), ('82', 'jVyir^6Rsl$MlQdH3D^3gWh9bYzvyMvGiE80v#Oq@6o*xJfOi&', '2014-10-14 21:03:01', '1', '12');
COMMIT;

-- ----------------------------
--  Table structure for `categories`
-- ----------------------------
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `meta_keywords` varchar(255) NOT NULL,
  `meta_description` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`),
  KEY `categories_63f17a16` (`parent_id`),
  KEY `categories_42b06ff6` (`lft`),
  KEY `categories_91543e5a` (`rght`),
  KEY `categories_efd07f28` (`tree_id`),
  KEY `categories_2a8f42e8` (`level`),
  CONSTRAINT `parent_id_refs_id_d28b8177` FOREIGN KEY (`parent_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `categories`
-- ----------------------------
BEGIN;
INSERT INTO `categories` VALUES ('30', 'Очки', 'ochki', 'Очки', '1', 'Очки', 'Очки', '2014-03-29 23:51:09', '2014-03-29 23:51:09', null, '1', '2', '6', '0'), ('34', 'Крестики', 'krestiki', 'крестики описание категории', '1', '', 'крестики', '2014-04-23 09:17:33', '2014-04-23 09:17:33', null, '1', '2', '8', '0');
COMMIT;

-- ----------------------------
--  Table structure for `characteristics`
-- ----------------------------
DROP TABLE IF EXISTS `characteristics`;
CREATE TABLE `characteristics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `characteristic_type_id` int(11) NOT NULL,
  `value` varchar(255) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`,`characteristic_type_id`),
  KEY `characteristics_4fc2fbf7` (`characteristic_type_id`),
  KEY `characteristics_bb420c12` (`product_id`),
  CONSTRAINT `characteristic_type_id_refs_id_ec03cb9b` FOREIGN KEY (`characteristic_type_id`) REFERENCES `characteristics_type` (`id`),
  CONSTRAINT `product_id_refs_id_e49775a` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `characteristics`
-- ----------------------------
BEGIN;
INSERT INTO `characteristics` VALUES ('1', '7', '29', '13'), ('2', '7', '32', '12');
COMMIT;

-- ----------------------------
--  Table structure for `characteristics_type`
-- ----------------------------
DROP TABLE IF EXISTS `characteristics_type`;
CREATE TABLE `characteristics_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `characteristics_type`
-- ----------------------------
BEGIN;
INSERT INTO `characteristics_type` VALUES ('1', 'Вес'), ('7', 'Длина'), ('4', 'Рабочий диапазон'), ('6', 'Размер'), ('2', 'Размеры'), ('5', 'Сенсорный экран'), ('3', 'Тип');
COMMIT;

-- ----------------------------
--  Table structure for `checkout_order`
-- ----------------------------
DROP TABLE IF EXISTS `checkout_order`;
CREATE TABLE `checkout_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `shipping_name` varchar(50) NOT NULL,
  `shipping_address_1` varchar(50) NOT NULL,
  `shipping_city` varchar(50) NOT NULL,
  `date` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `ip_address` char(15) NOT NULL,
  `last_updated` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `transaction_id` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkout_order_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_6abbfa5fa34ddcf1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `checkout_order`
-- ----------------------------
BEGIN;
INSERT INTO `checkout_order` VALUES ('1', 'greenteamer@bk.ru', '89138886899', 'Александр', 'Ленина 42 56 ', 'Северск', '2014-04-23 21:52:34', '1', '127.0.0.1', '2014-04-23 21:52:34', '1', '738421'), ('2', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ленина 42 56 ', 'Северск', '2014-04-24 02:14:47', '1', '127.0.0.1', '2014-04-24 02:14:47', '1', '640555'), ('3', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-24 02:18:28', '1', '127.0.0.1', '2014-04-24 02:18:28', '1', '597805'), ('4', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:19:46', '1', '127.0.0.1', '2014-04-26 21:19:46', '1', '864424'), ('5', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:21:13', '1', '127.0.0.1', '2014-04-26 21:21:13', '1', '77823'), ('6', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:28:00', '1', '127.0.0.1', '2014-04-26 21:28:00', '1', '847893'), ('7', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:34:45', '1', '127.0.0.1', '2014-04-26 21:34:45', '1', '991934'), ('8', 'teamer777@icloud.com', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:36:51', '1', '127.0.0.1', '2014-04-26 21:36:51', '1', '694697'), ('9', 'teamer777@icloud.com', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:38:14', '1', '127.0.0.1', '2014-04-26 21:38:14', '1', '405132'), ('10', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:38:52', '1', '127.0.0.1', '2014-04-26 21:38:52', '1', '83219'), ('11', 'teamer777@icloud.com', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:39:32', '1', '127.0.0.1', '2014-04-26 21:39:32', '1', '121666'), ('12', 'greenteamer@bk.ru', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:43:37', '1', '127.0.0.1', '2014-04-26 21:43:37', '1', '898055'), ('13', 'teamer777@icloud.com', '79264629960', 'Александр', 'Ул.  Ленина ', 'Северск', '2014-04-26 21:45:25', '1', '127.0.0.1', '2014-04-26 21:45:25', '1', '405261');
COMMIT;

-- ----------------------------
--  Table structure for `checkout_orderitem`
-- ----------------------------
DROP TABLE IF EXISTS `checkout_orderitem`;
CREATE TABLE `checkout_orderitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkout_orderitem_bb420c12` (`product_id`),
  KEY `checkout_orderitem_8337030b` (`order_id`),
  CONSTRAINT `order_id_refs_id_244a7339ca5e532c` FOREIGN KEY (`order_id`) REFERENCES `checkout_order` (`id`),
  CONSTRAINT `product_id_refs_id_46388334c40cb681` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `checkout_orderitem`
-- ----------------------------
BEGIN;
INSERT INTO `checkout_orderitem` VALUES ('1', '13', '1', '3123.00', '1'), ('2', '12', '4', '123.00', '1'), ('3', '11', '3', '1111.00', '1'), ('4', '13', '6', '3123.00', '2'), ('5', '12', '1', '123.00', '2'), ('6', '12', '1', '123.00', '3'), ('7', '12', '1', '123.00', '4'), ('8', '11', '4', '1111.00', '4'), ('9', '13', '1', '3123.00', '5'), ('10', '12', '1', '123.00', '6'), ('11', '13', '1', '3123.00', '7'), ('12', '13', '1', '3123.00', '8'), ('13', '12', '1', '123.00', '9'), ('14', '11', '1', '1111.00', '10'), ('15', '11', '1', '1111.00', '11'), ('16', '13', '1', '3123.00', '12'), ('17', '13', '1', '3123.00', '13');
COMMIT;

-- ----------------------------
--  Table structure for `checkout_orderoneclick`
-- ----------------------------
DROP TABLE IF EXISTS `checkout_orderoneclick`;
CREATE TABLE `checkout_orderoneclick` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(20) NOT NULL,
  `product_name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `checkout_orderoneclick`
-- ----------------------------
BEGIN;
INSERT INTO `checkout_orderoneclick` VALUES ('3', '66666666', ''), ('4', '123123123', 'FARM GIRL VINTAGE HAT'), ('5', 'Ваш телефон', 'FARM GIRL VINTAGE HAT'), ('6', 'Ваш телефон', 'FARM GIRL VINTAGE HAT'), ('7', '7777777', 'FARM GIRL VINTAGE HAT'), ('8', '888888', 'PLANET - HOLLYWOOD HAT 3'), ('9', '123123123', 'FARM GIRL VINTAGE HAT'), ('10', '14314', 'PLANET - HOLLYWOOD HAT 3'), ('11', '5464654564', 'FARM GIRL VINTAGE HAT'), ('12', '555555', 'PLANET - HOLLYWOOD HAT 3'), ('13', '213123', 'Крестик');
COMMIT;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_admin_log`
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` VALUES ('1', '2014-01-03 23:00:09', '1', '10', '6', 'Книги', '1', ''), ('2', '2014-01-03 23:00:37', '1', '13', '6', 'Размер', '1', ''), ('3', '2014-01-03 23:00:42', '1', '13', '7', 'Обложка', '1', ''), ('4', '2014-01-03 23:00:50', '1', '13', '8', 'Страниц', '1', ''), ('5', '2014-01-03 23:02:34', '1', '11', '3', 'Исцеление верой', '1', ''), ('6', '2014-01-03 23:03:44', '1', '11', '3', 'Исцеление верой', '2', 'Изменен is_bestseller и is_featured.'), ('7', '2014-01-03 23:04:12', '1', '11', '3', 'Исцеление верой', '2', 'Добавлен product image \"ProductImage object\".'), ('8', '2014-01-03 23:22:04', '1', '11', '3', 'Исцеление верой', '2', 'Deleted product image \"ProductImage object\".'), ('9', '2014-01-03 23:22:16', '1', '11', '3', 'Исцеление верой', '2', 'Changed default for product image \"ProductImage object\".'), ('10', '2014-01-04 01:15:38', '1', '11', '4', 'Мир вам', '1', ''), ('11', '2014-01-04 20:46:36', '1', '10', '7', 'Биографии и свидетельства', '1', ''), ('12', '2014-01-04 20:48:02', '1', '10', '8', 'Библии', '1', ''), ('13', '2014-01-04 20:48:26', '1', '10', '6', 'Книги', '2', 'Ни одно поле не изменено.'), ('14', '2014-01-04 20:51:28', '1', '10', '7', 'Биографии и свидетельства', '3', ''), ('15', '2014-01-04 20:51:28', '1', '10', '6', 'Книги', '3', ''), ('16', '2014-01-04 20:52:14', '1', '10', '9', 'Книги', '1', ''), ('17', '2014-01-04 20:52:37', '1', '10', '10', 'Биографии и свидетельства', '1', ''), ('18', '2014-01-04 20:52:51', '1', '10', '11', 'Богословие, история, учебные пособия', '1', ''), ('19', '2014-01-04 20:52:56', '1', '10', '11', 'Богословие, история, учебные пособия', '2', 'Ни одно поле не изменено.'), ('20', '2014-01-04 20:53:09', '1', '10', '12', 'Взаимоотношения, семья', '1', ''), ('21', '2014-01-04 20:53:21', '1', '10', '13', 'Воспитание детей', '1', ''), ('22', '2014-01-04 20:53:36', '1', '10', '14', 'Для женщин', '1', ''), ('23', '2014-01-04 20:53:46', '1', '10', '15', 'Для мужчин', '1', ''), ('24', '2014-01-04 20:54:16', '1', '10', '16', 'Для юношей и девушек', '1', ''), ('25', '2014-01-04 20:54:26', '1', '10', '17', 'Духовная война', '1', ''), ('26', '2014-01-04 20:54:39', '1', '10', '18', 'Душепопечение, консультирование', '1', ''), ('27', '2014-01-04 20:54:49', '1', '10', '19', 'Здоровье, исцеление', '1', ''), ('28', '2014-01-04 20:54:59', '1', '10', '20', 'Лидерство, наставничество', '1', ''), ('29', '2014-01-04 20:55:09', '1', '10', '21', 'Молитва, поклонение', '1', ''), ('30', '2014-01-04 20:55:20', '1', '10', '22', 'Проповеди', '1', ''), ('31', '2014-01-04 20:55:29', '1', '10', '23', 'Пророчества и видения', '1', ''), ('32', '2014-01-04 20:55:39', '1', '10', '24', 'Служение в церкви, домашние группы', '1', ''), ('33', '2014-01-04 20:55:50', '1', '10', '25', 'Финансы, бизнес, успех', '1', ''), ('34', '2014-01-04 20:55:59', '1', '10', '26', 'Христианская жизнь', '1', ''), ('35', '2014-01-04 20:56:12', '1', '10', '27', 'Художественная литература', '1', ''), ('36', '2014-01-05 00:54:58', '1', '7', '1', '/caontact/ -- Контакты', '1', ''), ('37', '2014-01-05 00:56:36', '1', '7', '1', '/caontact/ -- Контакты', '2', 'Изменен content.'), ('38', '2014-01-05 00:57:34', '1', '7', '1', '/caontact/ -- Контакты', '2', 'Изменен content.'), ('39', '2014-01-05 00:59:30', '1', '7', '1', '/contact/ -- Контакты', '2', 'Изменен url.'), ('40', '2014-01-05 01:10:18', '1', '7', '2', '/dostavka/ -- Доставка', '1', ''), ('41', '2014-01-05 01:13:16', '1', '7', '3', '/o-nas/ -- О нас', '1', ''), ('42', '2014-01-05 09:23:41', '1', '11', '4', 'Мир вам', '2', 'Изменен categories.'), ('43', '2014-01-05 09:23:49', '1', '11', '3', 'Исцеление верой', '2', 'Изменен categories.'), ('44', '2014-02-03 21:13:30', '1', '11', '4', 'Мир вам', '2', 'Добавлен product image \"ProductImage object\".'), ('45', '2014-03-29 22:27:58', '1', '10', '10', 'Биографии и свидетельства', '3', ''), ('46', '2014-03-29 22:27:58', '1', '10', '11', 'Богословие, история, учебные пособия', '3', ''), ('47', '2014-03-29 22:27:58', '1', '10', '12', 'Взаимоотношения, семья', '3', ''), ('48', '2014-03-29 22:27:58', '1', '10', '13', 'Воспитание детей', '3', ''), ('49', '2014-03-29 22:27:58', '1', '10', '14', 'Для женщин', '3', ''), ('50', '2014-03-29 22:27:58', '1', '10', '15', 'Для мужчин', '3', ''), ('51', '2014-03-29 22:27:58', '1', '10', '16', 'Для юношей и девушек', '3', ''), ('52', '2014-03-29 22:27:58', '1', '10', '17', 'Духовная война', '3', ''), ('53', '2014-03-29 22:27:58', '1', '10', '18', 'Душепопечение, консультирование', '3', ''), ('54', '2014-03-29 22:27:58', '1', '10', '19', 'Здоровье, исцеление', '3', ''), ('55', '2014-03-29 22:27:58', '1', '10', '20', 'Лидерство, наставничество', '3', ''), ('56', '2014-03-29 22:27:58', '1', '10', '21', 'Молитва, поклонение', '3', ''), ('57', '2014-03-29 22:27:58', '1', '10', '22', 'Проповеди', '3', ''), ('58', '2014-03-29 22:27:58', '1', '10', '23', 'Пророчества и видения', '3', ''), ('59', '2014-03-29 22:27:58', '1', '10', '24', 'Служение в церкви, домашние группы', '3', ''), ('60', '2014-03-29 22:27:58', '1', '10', '25', 'Финансы, бизнес, успех', '3', ''), ('61', '2014-03-29 22:27:58', '1', '10', '27', 'Художественная литература', '3', ''), ('62', '2014-03-29 22:30:32', '1', '10', '28', 'Обувь', '1', ''), ('63', '2014-03-29 22:30:52', '1', '11', '4', 'Мир вам', '2', 'Изменен categories.'), ('64', '2014-03-29 22:30:56', '1', '11', '3', 'Исцеление верой', '2', 'Изменен categories.'), ('65', '2014-03-29 22:34:21', '1', '11', '4', 'Мир вам', '2', 'Удален product image \"ProductImage object\".'), ('66', '2014-03-29 23:50:24', '1', '10', '8', 'Библии', '3', ''), ('67', '2014-03-29 23:50:24', '1', '10', '9', 'Книги', '3', ''), ('68', '2014-03-29 23:50:24', '1', '10', '26', 'Христианская жизнь', '3', ''), ('69', '2014-03-29 23:50:54', '1', '10', '29', 'Сумки', '1', ''), ('70', '2014-03-29 23:51:09', '1', '10', '30', 'Очки', '1', ''), ('71', '2014-03-29 23:51:36', '1', '10', '31', 'Обувь 1', '1', ''), ('72', '2014-03-29 23:51:48', '1', '10', '32', 'Обувь 2', '1', ''), ('73', '2014-03-29 23:52:01', '1', '10', '32', 'Обувь 2', '2', 'Изменен parent.'), ('74', '2014-03-30 00:05:29', '1', '11', '4', 'Мир вам', '3', ''), ('75', '2014-03-30 00:05:29', '1', '11', '3', 'Исцеление верой', '3', ''), ('76', '2014-03-30 00:11:20', '1', '13', '7', 'Обложка', '3', ''), ('77', '2014-03-30 00:11:20', '1', '13', '8', 'Страниц', '3', ''), ('78', '2014-03-30 00:23:43', '1', '11', '5', 'LIGHT HOUSE T-SHIRT', '1', ''), ('79', '2014-03-30 00:24:18', '1', '11', '5', 'LIGHT HOUSE T-SHIRT', '2', 'Изменен is_featured.'), ('80', '2014-03-30 00:24:35', '1', '11', '5', 'LIGHT HOUSE T-SHIRT', '2', 'Изменен is_bestseller и is_featured.'), ('81', '2014-03-30 00:25:05', '1', '11', '5', 'LIGHT HOUSE T-SHIRT', '2', 'Изменен is_featured.'), ('82', '2014-03-30 00:52:02', '1', '11', '6', 'INSPIRED DRESS SANDALS1', '1', ''), ('83', '2014-03-30 00:53:23', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '1', ''), ('84', '2014-03-31 00:24:35', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '2', 'Изменен is_bestseller.'), ('85', '2014-03-31 00:27:30', '1', '11', '8', 'ADIDAS ORIGINALS-SHIRT', '1', ''), ('86', '2014-03-31 00:29:23', '1', '10', '33', 'Головные уборы', '1', ''), ('87', '2014-03-31 00:30:33', '1', '11', '9', 'INSPIRED DRESS SANDALS2', '1', ''), ('88', '2014-03-31 00:33:09', '1', '11', '10', 'FARM GIRL VINTAGE HAT', '1', ''), ('89', '2014-04-07 15:47:53', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '2', 'Изменены image для product image \"ProductImage object\".'), ('90', '2014-04-07 15:49:59', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '2', 'Изменены image для product image \"ProductImage object\".'), ('91', '2014-04-07 15:50:57', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '2', 'Ни одно поле не изменено.'), ('92', '2014-04-07 15:52:26', '1', '11', '6', 'INSPIRED DRESS SANDALS1', '2', 'Изменены image для product image \"ProductImage object\".'), ('93', '2014-04-07 15:53:21', '1', '11', '5', 'LIGHT HOUSE T-SHIRT', '2', 'Изменены image для product image \"ProductImage object\".'), ('94', '2014-04-07 23:52:25', '1', '11', '7', 'PLANET - HOLLYWOOD HAT 3', '2', 'Изменены image для product image \"ProductImage object\".'), ('95', '2014-04-09 00:40:30', '1', '11', '9', 'INSPIRED DRESS SANDALS2', '2', 'Изменены image для product image \"ProductImage object\".'), ('96', '2014-04-09 02:09:21', '1', '11', '10', 'FARM GIRL VINTAGE HAT', '2', 'Добавлен product image \"ProductImage object\". Добавлен product image \"ProductImage object\". Добавлен product image \"ProductImage object\".'), ('97', '2014-04-09 15:05:32', '1', '22', '1', 'OrderOneClick object', '1', ''), ('98', '2014-04-09 17:22:53', '1', '22', '1', 'OrderOneClick object', '3', ''), ('99', '2014-04-13 01:45:45', '1', '11', '10', 'FARM GIRL VINTAGE HAT', '2', 'Изменен articul.'), ('100', '2014-04-13 01:50:47', '1', '11', '10', 'FARM GIRL VINTAGE HAT', '2', 'Изменен meta_keywords.'), ('101', '2014-04-13 01:51:36', '1', '11', '10', 'FARM GIRL VINTAGE HAT', '2', 'Ни одно поле не изменено.'), ('102', '2014-04-20 02:39:21', '1', '11', '11', 'Очки', '1', ''), ('103', '2014-04-20 02:39:30', '1', '11', '11', 'Очки', '2', 'Изменены default для product image \"ProductImage object\". Изменены default для product image \"ProductImage object\".'), ('104', '2014-04-23 09:11:08', '1', '25', '1', 'Очки', '1', ''), ('105', '2014-04-23 09:17:33', '1', '10', '34', 'Крестики', '1', ''), ('106', '2014-04-23 09:20:06', '1', '11', '12', 'Крестик', '1', ''), ('107', '2014-04-23 09:20:09', '1', '25', '1', 'Крестик', '2', 'Изменен product.'), ('108', '2014-04-23 09:22:27', '1', '11', '13', 'Еще крестик', '1', ''), ('109', '2014-04-23 09:22:29', '1', '25', '2', 'Еще крестик', '1', ''), ('110', '2014-04-23 10:04:59', '1', '11', '13', 'Еще крестик', '2', 'Изменен brand.'), ('111', '2014-04-23 10:08:00', '1', '11', '13', 'Еще крестик', '2', 'Изменен brand и description.'), ('112', '2014-04-23 10:08:44', '1', '11', '12', 'Крестик', '2', 'Изменен brand и description.'), ('113', '2014-04-23 10:27:56', '1', '10', '33', 'Головные уборы', '3', ''), ('114', '2014-04-23 10:27:56', '1', '10', '3', 'Категория 2', '3', ''), ('115', '2014-04-23 10:27:56', '1', '10', '28', 'Обувь', '3', ''), ('116', '2014-04-23 10:27:56', '1', '10', '31', 'Обувь 1', '3', ''), ('117', '2014-04-23 10:27:56', '1', '10', '32', 'Обувь 2', '3', ''), ('118', '2014-04-23 10:27:56', '1', '10', '2', 'Подкатегория 1', '3', ''), ('119', '2014-04-23 10:27:56', '1', '10', '5', 'Подкатегория 3', '3', ''), ('120', '2014-04-23 10:27:56', '1', '10', '4', 'Сотовые телефоны', '3', ''), ('121', '2014-04-23 10:27:56', '1', '10', '29', 'Сумки', '3', ''), ('122', '2014-04-23 10:28:10', '1', '10', '1', 'Категория 1', '3', ''), ('123', '2014-04-26 12:18:42', '1', '11', '13', 'Еще крестик', '2', 'Добавлен product image \"ProductImage object\".'), ('124', '2014-04-26 12:20:12', '1', '11', '12', 'Крестик', '2', 'Добавлен product image \"ProductImage object\". Добавлен product image \"ProductImage object\". Добавлен product image \"ProductImage object\". Добавлен product image \"ProductImage object\".'), ('125', '2014-04-26 12:31:38', '1', '13', '7', 'Длина', '1', ''), ('126', '2014-04-26 12:31:53', '1', '11', '13', 'Еще крестик', '2', 'Добавлен characteristic \"Characteristic object\".'), ('127', '2014-04-26 12:35:04', '1', '11', '12', 'Крестик', '2', 'Добавлен characteristic \"Characteristic object\".');
COMMIT;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'permission', 'auth', 'permission'), ('2', 'group', 'auth', 'group'), ('3', 'user', 'auth', 'user'), ('4', 'content type', 'contenttypes', 'contenttype'), ('5', 'session', 'sessions', 'session'), ('6', 'site', 'sites', 'site'), ('7', 'flat page', 'flatpages', 'flatpage'), ('8', 'log entry', 'admin', 'logentry'), ('9', 'migration history', 'south', 'migrationhistory'), ('10', 'category', 'catalog', 'category'), ('11', 'product', 'catalog', 'product'), ('12', 'product image', 'catalog', 'productimage'), ('13', 'characteristic type', 'catalog', 'characteristictype'), ('14', 'characteristic', 'catalog', 'characteristic'), ('15', 'cart item', 'cart', 'cartitem'), ('16', 'user profile', 'accounts', 'userprofile'), ('17', 'order', 'checkout', 'order'), ('18', 'order item', 'checkout', 'orderitem'), ('19', 'Post', 'news', 'news'), ('20', 'search term', 'search', 'searchterm'), ('21', 'kv store', 'thumbnail', 'kvstore'), ('22', 'order one click', 'checkout', 'orderoneclick'), ('23', 'dashboard preferences', 'dashboard', 'dashboardpreferences'), ('24', 'bookmark', 'menu', 'bookmark'), ('25', 'slider', 'slider', 'slider');
COMMIT;

-- ----------------------------
--  Table structure for `django_flatpage`
-- ----------------------------
DROP TABLE IF EXISTS `django_flatpage`;
CREATE TABLE `django_flatpage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `enable_comments` tinyint(1) NOT NULL,
  `template_name` varchar(70) NOT NULL,
  `registration_required` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_flatpage_a4b49ab` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_flatpage`
-- ----------------------------
BEGIN;
INSERT INTO `django_flatpage` VALUES ('1', '/contact/', 'Контакты', '<p>Если вас заинтересовали наши книги, вы можете ОЧЕНЬ ЛЕГКО с нами связаться.</p>\r\n\r\n<p>190000, г. Томск,  Главпочтамт, а/я 43,  «Христианская миссия»</p>\r\n\r\n<p>Телефон: +7 (901) 320-01-91 , +7 (812) 320-01-91 </p>\r\n\r\n<p>Подробно об условиях доставки и скидках можно узнать на странице нашего интернет-магазина</p>', '0', '', '0'), ('2', '/dostavka/', 'Доставка', '<h2>КАК ОФОРМИТЬ САМОВЫВОЗ</h2>\r\n\r\n<p>1. Заказ на самовывоз можно оформить в любой день, по телефону с 10.00 до 18.00. </p>\r\n<p>2. Заказ на самовывоз после 18.00 не оформляется. </p>\r\n<p>3. Заказ на самовывоз нельзя оформить, как предварительный заказ, на время с 19.00 и позже, даже если заказ оформляется до 18.00. </p>\r\n<p>4. Заказ можно сделать придя в офис, в любой день с 10.00 до 18.00. </p>\r\n<p>5. После 18.00 заказы в офисе не оформляются. </p>\r\n', '0', '', '0'), ('3', '/o-nas/', 'О нас', '<p>Промышленная группа «Базовый Элемент» объединяет около 100 российских и международных предприятий, работающих в энергетической, горнодобывающей, металлургической, машиностроительной, авиационной, финансовой, сельскохозяйственной и других отраслях.  </p>\r\n\r\n<p>Обширный и диверсифицированный портфель активов «Базового Элемента» представляет собой единую бизнес-структуру, предприятия которой эффективно взаимодействуют между собой, реализуя партнерские программы, позволяющие усилить конкурентные преимущества отдельных компаний группы и холдинга в целом.</p>\r\n\r\n<p>В состав «Базового Элемента» входят лидеры крупнейших промышленных отраслей. Среди них – ведущий мировой производитель алюминия РУСАЛ, крупнейший в России частный производитель электроэнергии «ЕвроСибЭнерго» (входят в группу En+), автомобильный холдинг номер один в России «Группа ГАЗ» (входит в холдинг «Русские машины»), а также компания «Главстрой», лидер строительного рынка Москвы и Санкт-Петербурга.</p>\r\n\r\n<p>Масштабная и активная деятельность предприятий «Базового Элемента» вносит существенный вклад в развитие российской промышленности, экономики и социальной инфраструктуры. Бизнес-группа обеспечивает около 1% ВВП России и инвестирует значительные средства в развитие регионов страны. «Базовый Элемент» – один из крупнейших работодателей в России. В течение последних пяти лет компания создала более 15 тыс. новых рабочих мест и планирует создать еще несколько десятков тысяч рабочих мест к 2025 году.</p>\r\n\r\n<p>Стратегия роста «Базового Элемента» направлена на укрепление лидерских позиций предприятий группы за счет повышения эффективности производства, расширения промышленной базы и реализации крупных инновационных проектов, а также на содействие социально-экономическому развитию территорий своего присутствия  и обеспечение экологической безопасности производства. </p>', '0', '', '0');
COMMIT;

-- ----------------------------
--  Table structure for `django_flatpage_sites`
-- ----------------------------
DROP TABLE IF EXISTS `django_flatpage_sites`;
CREATE TABLE `django_flatpage_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flatpage_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `flatpage_id` (`flatpage_id`,`site_id`),
  KEY `django_flatpage_sites_dedefef8` (`flatpage_id`),
  KEY `django_flatpage_sites_6223029` (`site_id`),
  CONSTRAINT `flatpage_id_refs_id_c0e84f5a` FOREIGN KEY (`flatpage_id`) REFERENCES `django_flatpage` (`id`),
  CONSTRAINT `site_id_refs_id_4e3eeb57` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_flatpage_sites`
-- ----------------------------
BEGIN;
INSERT INTO `django_flatpage_sites` VALUES ('4', '1', '1'), ('5', '2', '1'), ('6', '3', '1');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_session`
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('0a3fdd80ca7ea008c705c0f295fbb3a1', 'NjI3ZGE5OTQ2NjVkYWZiMjU2YzA5ZGE0ODk4YTJkODJkN2I1NDMxYzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMnYpU2Imb3lRYyQqQDlZNXpqdjEyaG1ROEEzVTNsY3FA\nVksmVCp6ZENFUDlyKGNjdFU4dS4=\n', '2014-07-28 06:23:50'), ('0de48e91545b6ecf768a457975212908', 'OTZjM2ZhYmY4NTYxYzQ4ZWJlYjk3ODFkOWZmYWQxMjE1MWQwYzBmMjqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMmpWeWlyXjZSc2wkTWxRZEgzRF4zZ1doOWJZenZ5TXZH\naUU4MHYjT3FANm8qeEpmT2kmdS4=\n', '2015-01-12 21:03:01'), ('1e2134ac06cac565a76b912463c00ab3', 'YTI0YjIwMTRiNzIzZTRjOWU1MzJlMTAwMjc2OGRjZjRiNTFhNzgxMDqAAn1xAVUHY2FydF9pZHEC\nVTJqc1UwRFV5UnJnKmtJOHpMSFBlQVpmSVc3WEh6UTFHTXl3bkdGSlAxKUxsTiUoKUZnJXMu\n', '2015-01-24 22:34:12'), ('1ec6a19d02c291184656b9036434baf6', 'MjRjMWM5ZWFkZjNkZjcxZjJiOGNkNWU2YjlkMDM1ZmUyNjQxZDUzNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVCnRl\nc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTIwVmZJRnc0UEgmOXRpSlMzJUJCWWU0VSl3UWlh\nTzNUKkRBR1QpdG5laXNzRHVOa1dKUlUNX2F1dGhfdXNlcl9pZIoBAXUu\n', '2014-07-12 02:05:35'), ('237370fb7e9d4eda501f400b2cce41f1', 'ZDRmZTY5MzUzZDlmYWZjY2Q2MTgyODFmZjRkYTBlYTY0ZWZkNmE4ODqAAn1xAVUHY2FydF9pZHEC\nVTJpVlAhMCZ5a2hkaWRQKSowenVGRXFpQ2h5eV56UkVNNlgqY14oeGlOdUl2VnU5SypLeXMu\n', '2014-06-22 13:59:26'), ('38fb58ee73d9492ec8f98ed33e6828ac', 'YzdkMzZjZGIwYWUyMmU0NzE1YWFmNWZkMGU0YmEzYTc3NjgzZTRjNTqAAn1xAVUHY2FydF9pZHEC\nVTJVWjlRcVVtKmdNRDNAVmt6a2JEQVUkayZWT0lDKkRsb3ppckNzI1NWanZAJGw2Y3ojbHMu\n', '2014-04-05 01:42:48'), ('3e9186e8a4dac849f07f867a098a027e', 'YmM4MTIxNTNmZTFhYjdhM2UzZDgwNWE4MGEyNjFkZDI2ZTgzZGIyMDqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVCnRlc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTJINFJidDEkWEdaNGEwcmJh\nVHFZRGJ6UChFZyRWRGYhOVlHdWhZWkVvNGN4JG9eM2E4VlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlk\namFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu\n', '2014-07-10 18:59:46'), ('3faac7a1be377e0802076e56191365f6', 'MDJlOTM3ZWI1OWFkYmU0M2VlOGE3Nzg4ZGJjN2U0NjQ2MjgxZjk3MDqAAn1xAVUHY2FydF9pZHEC\nVTJYcjlZdlkyTSNSeCU0ejJWUXUmdmxedkNzcW9lZXFuIzZpWHE5Q0RFY1ZIJlVIMUZoenMu\n', '2014-07-14 16:13:06'), ('43bec300ec9bca1b26c773d88414f9e2', 'MTlkZTRhYzA4NmQ1NGM3ZWEyMWY0YjA4MjI1NGRiNjE5ZGNlMjc1YTqAAn1xAVUHY2FydF9pZHEC\nVTJpcmRxb3Y3dSVYMFB4TmhnU1NWMFQyb0ghRXBwU0lrMXg5TDhuUCRReVdObmhRUSp1dXMu\n', '2014-07-21 15:27:59'), ('470c895e58af2785580259556e48ba8b', 'NzZmODI4YTdiZjMwODExZWE0ZWJhYTM3MzhhODA3YTkzMzE3MDEyODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVCnRl\nc3Rjb29raWVVBndvcmtlZHECVQlfbWVzc2FnZXNdcQMoY2RqYW5nby5jb250cmliLm1lc3NhZ2Vz\nLnN0b3JhZ2UuYmFzZQpNZXNzYWdlCnEEKYFxBX1xBihVCmV4dHJhX3RhZ3NxB1gAAAAAVQdtZXNz\nYWdlcQhYRQAAAHByb2R1Y3QgIkxJR0hUIEhPVVNFIFQtU0hJUlQiINCx0YvQuyDRg9GB0L/QtdGI\n0L3QviDQtNC+0LHQsNCy0LvQtdC9LlUFbGV2ZWxxCUsUdWJoBCmBcQp9cQsoaAdYAAAAAGgIWEMA\nAABwcm9kdWN0ICJMSUdIVCBIT1VTRSBULVNISVJUIiDQsdGL0Lsg0YPRgdC/0LXRiNC90L4g0LjQ\nt9C80LXQvdC10L0uaAlLFHViaAQpgXEMfXENKGgHWAAAAABoCFhDAAAAcHJvZHVjdCAiTElHSFQg\nSE9VU0UgVC1TSElSVCIg0LHRi9C7INGD0YHQv9C10YjQvdC+INC40LfQvNC10L3QtdC9LmgJSxR1\nYmgEKYFxDn1xDyhoB1gAAAAAaAhYQwAAAHByb2R1Y3QgIkxJR0hUIEhPVVNFIFQtU0hJUlQiINCx\n0YvQuyDRg9GB0L/QtdGI0L3QviDQuNC30LzQtdC90LXQvS5oCUsUdWJoBCmBcRB9cREoaAdYAAAA\nAGgIWEkAAABwcm9kdWN0ICJJTlNQSVJFRCBEUkVTUyBTQU5EQUxTMSIg0LHRi9C7INGD0YHQv9C1\n0YjQvdC+INC00L7QsdCw0LLQu9C10L0uaAlLFHViaAQpgXESfXETKGgHWAAAAABoCFhKAAAAcHJv\nZHVjdCAiUExBTkVUIC0gSE9MTFlXT09EIEhBVCAzIiDQsdGL0Lsg0YPRgdC/0LXRiNC90L4g0LTQ\nvtCx0LDQstC70LXQvS5oCUsUdWJoBCmBcRR9cRUoaAdYAAAAAGgIWEgAAABwcm9kdWN0ICJQTEFO\nRVQgLSBIT0xMWVdPT0QgSEFUIDMiINCx0YvQuyDRg9GB0L/QtdGI0L3QviDQuNC30LzQtdC90LXQ\nvS5oCUsUdWJoBCmBcRZ9cRcoaAdYAAAAAGgIWEgAAABwcm9kdWN0ICJBRElEQVMgT1JJR0lOQUxT\nLVNISVJUIiDQsdGL0Lsg0YPRgdC/0LXRiNC90L4g0LTQvtCx0LDQstC70LXQvS5oCUsUdWJoBCmB\ncRh9cRkoaAdYAAAAAGgIWEkAAABwcm9kdWN0ICJJTlNQSVJFRCBEUkVTUyBTQU5EQUxTMiIg0LHR\ni9C7INGD0YHQv9C10YjQvdC+INC00L7QsdCw0LLQu9C10L0uaAlLFHViaAQpgXEafXEbKGgHWAAA\nAABoCFhHAAAAcHJvZHVjdCAiRkFSTSBHSVJMIFZJTlRBR0UgSEFUIiDQsdGL0Lsg0YPRgdC/0LXR\niNC90L4g0LTQvtCx0LDQstC70LXQvS5oCUsUdWJlVQ1fYXV0aF91c2VyX2lkigEBVQdjYXJ0X2lk\nVTJxXkwoa01FOTkmbnZAUk8zVDRiaiphTmh1M3M0MzE2bVJzdSluMGZFdk8qanJqNUJnNHUu\n', '2014-06-29 01:27:23'), ('5059b819e4f60e14c59b2cbc8d98de8e', 'NjliNGI5ZTg4NzI3OTg0Yzk3YmU3YmIxOWIwMGMwMjQ1YTBmNjgxZjqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVCnRlc3Rjb29raWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMmZJVWQkVDkzMCRTUDRs\nRDRRcyUxKmRXZzFeNXJhR0N5MTF6WFJYUVlWMnlYYSQ1T21pVRJfYXV0aF91c2VyX2JhY2tlbmRV\nKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kdS4=\n', '2014-07-23 02:51:20'), ('57eb18b25dc4b59ff11cdcb7a5760f95', 'MGRhZmNhZDNlNTUzMTYyY2IwZWFiMWM1NjczMDE0Zjc5ODk2ZjQ4NzqAAn1xAVUHY2FydF9pZHEC\nVTJnYlVZcShVdU1pT04lam1ZUlc5MTN3QyhSbWxedCgoSFUoZzNiOSY1Sm5VZmdPNzdiVHMu\n', '2014-06-29 14:50:31'), ('58e46e0afe645f483dc909d96d9a5edd', 'YTJiOTA5YjY1NzY1NWVjMzY3YTUwYmUzMTE5NWJhODk4MDcwN2JkZTqAAn1xAVUHY2FydF9pZHEC\nVTJrNGlnNlNIMUBiOFBWcDE0TXZ2TWFYM25Xd0lOdm9AaHBRbUZAdUdtRGokdHlzZ09IeHMu\n', '2014-12-27 21:40:37'), ('5f45e6d773c4207296893106559be870', 'NmRhNmI1OWU1NWIyN2IzMmYyMjA5ZjY2NTY2Yjk3N2VmY2UyYzlkNTqAAn1xAVUHY2FydF9pZHEC\nVTJSRWpoS0twVm5UUTBPRUJCSDNjdSFuY2NTI21HZ3dOb25XUkRvJCFEZGJuQmhAWHchMXMu\n', '2014-06-30 15:11:51'), ('64d933c5d4b184dde9d22fabbe19e610', 'OWRmNDI1OTNhOTQ4NGM1YTA2MTY4NWQ4MWQwODcxN2I4YzRlYWVjZDqAAn1xAVUHY2FydF9pZHEC\nVTJCRm1BJEJVJCNmQ2ZDMHVnZndmRHAyJVdsMmQybWJDWmRTV1U5cERDTk1aTENsOE5nOHMu\n', '2014-04-05 01:39:23'), ('67dcdb76e358f1624329bc9ffe8a7ff8', 'MWQ4NzY0YjU1MWZkNmU2YzhlYzMyODQwYTY5YThmNmQ3N2YyMTU3NjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQdjYXJ0X2lkVTJoMyM0QSZCSzNYISFFWSNpYm9tNjVxcmdsNzUxMk5kIUNyTyZsWGJVNjFvJTc4\nWHZVMVUNX2F1dGhfdXNlcl9pZHEEigEBdS4=\n', '2014-07-27 20:48:44'), ('6de8a962db40e2c85a4489be75e10952', 'MDQzZDE0MThjOThjNDE4ZjE0MGI3ZTJlNjg5NDZmNmE3OGIyZDJjYzqAAn1xAVUHY2FydF9pZHEC\nVTJqTkNCYk5OcUI5QHkyaF5ZbCk4blBHT0haTVlZZHRQcThvKjQzb1NXJm40dTNNJUhEMnMu\n', '2014-04-05 01:42:58'), ('72b421fb0d67ba35729e2be72aae5d56', 'ZDZhOTJmMzMwMDg3MWY5NTBkOGEyZTIwZDg0N2JkMjU1Y2FkZTU1ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVB2Nh\ncnRfaWRVMlZTUG4zQ2xqVWRhTllCIW4qd0tteENvUGQybUFHN09aS3owTGN3dDZhS0BlVkgyUyZl\nVQ1fYXV0aF91c2VyX2lkigEBVQ9kamFuZ29fbGFuZ3VhZ2VYAgAAAHJ1dS4=\n', '2014-04-06 16:15:59'), ('7c93d52324ea935bd71d0d921167ee2f', 'NDcxNDZmY2I4NDQ2ZTZhZjc4NDlkZDhmZTY3ODFjNTc2MDY5MDU1YzqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVCnRlc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTJHcWtEbUxuTmkkdUJDJCpH\ncG43MkMkbHZzcUwyQCZia1pVVGRKKklBIyh2YnpRI1hpdVUSX2F1dGhfdXNlcl9iYWNrZW5kVSlk\namFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu\n', '2014-05-04 21:14:00'), ('81b038703cba8573ded3ed03c264c569', 'YjQ2NDk1Y2MzMGRkMDU0M2Q4MWRmZDY4NTM0MDY3MGJiOWRhYWNjZDqAAn1xAVUHY2FydF9pZHEC\nVTJvSlhDbil5TDBlKllncnRnQEFNbW1jKFhGdXFHJSF6am9vZm8mTUNOT1NKMWkmUDhBYXMu\n', '2014-07-19 19:26:06'), ('866f3522416ae939ca852673e33dce99', 'NGZjOWM4YzA3Y2RlMWY3NGIzNDYxODAzNmI0ZTIxYTc0M2NjYWFiZTqAAn1xAVUHY2FydF9pZHEC\nVTIoNVheNzd3KnlwazJ4Vk4kQChNdFBUaDBrZHFuVV5JeG11b0pHQ3k5Mk15N3BGSVVOOHMu\n', '2014-07-27 20:17:49'), ('88c85cab52a8cfc9aa18707c76114680', 'ZWNiMDgxODdmNGJjMzFiNGY2MGI5M2RlZDQzY2I1ZjUxNmE4ZDAwNTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVB2NhcnRfaWRVMkx6KlVWY0UjM1ZwZ0xVcCZsb0pvWUhsQWFQa0k2SjNZOVNaTW9K\nbXlmTjJmMHkkZ3BWVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5jb250cmliLmF1dGguYmFj\na2VuZHMuTW9kZWxCYWNrZW5kdS4=\n', '2014-04-15 07:50:34'), ('8b26e2e931ad4cb4f32805a18ff76597', 'MTY2Mjk0ODZjZTUyM2MwZWY2MDFjOTIxNDJkMWQ5YThlNzA4ZDBmYTqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMnFRKEohJEd6ekFGV3VpKlFGZSZqdXhEdHZoMGNpcXp0\nYiRLV0Y0dzJaWnozMldndSNOdS4=\n', '2014-07-25 02:22:32'), ('9683051367b89467d493989181540d8f', 'NzYxOTA0ODNlNjhiZjdiN2JiODg3ZTYyOTg5NTAzYWM5ZjUzOWE2MDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQdjYXJ0X2lkVTIkM2VaM24wdW5AT3BPXmFeXkdQUWpWNVNRRmdCaWFSOHp4NkM3eHQwKTFOV3BQ\nbWlvM1UNX2F1dGhfdXNlcl9pZHEEigEBdS4=\n', '2014-07-06 15:43:49'), ('969496e0365e4c193d5babd8d1a0baf3', 'ZTRlNTM4OTg4NTY2Y2NlNzNlNmFmY2I2NDVhNzJiNGE2YzNiODFiMzqAAn1xAVUHY2FydF9pZHEC\nVTIpWEcjTklUZWUpdVhDa2QpcihGN0hqS3hhRSZeXklCJiNSKiN1Xnd3Z3N5T15FeXlMMHMu\n', '2014-07-14 14:28:52'), ('96ed0acb96782f311c35b5e35588b110', 'ZjNiZDY1ZDY3NGU3Njg2OTM5ZDIzZmM2MmJkYmQwOGFhZWIxNGJhMDqAAn1xAVUHY2FydF9pZFUy\nMVhwZE5VJkYzOUc0VU5KdDdFVXdYaWpReEl4ejRETTByR0gkcDhjRl51emwzIWZwdnRzLg==\n', '2014-07-09 15:56:32'), ('a3e145307da13bbc3bf9bea9f66e3350', 'NTRhYWVmNzMxOTNhMjgxNzYxZmVjNjE4NDYyNDJjMjE2NDA5Njg2NDqAAn1xAVUHY2FydF9pZHEC\nVTJuKGxPWVAybjVVYVljZE9TMWo0NTRnSFgpZllLMVdZQHYoRCp1Nm50d0B3dHYhMkx6I3Mu\n', '2014-07-14 15:25:03'), ('a452362e5215fff5047b39d5e6934ef3', 'NDBhMTFjZTgwYjkwZDY0ODBiNzk1OTI2MjZmNDgwNDcyZjRiNGUyYTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQJVCnRlc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTJ0ak0mNnJlVTQmIWZPMFhQ\nMmtKdkhjeE5udHdRVkRQUXlJWXcpKndHZilxU2J4aFRiblUSX2F1dGhfdXNlcl9iYWNrZW5kVSlk\namFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu\n', '2014-04-05 01:38:36'), ('a8336db33fb765348d12a350bb2fba4f', 'MWZlYzg0NTRkNTc0NjI5NjA3ZDU3ODQ5NTRlNWFiN2U1OGUwODYwNDqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMnNZJFZsWHl1IzRQT2lqdHRseHRWcDkqZ3F2UTVCXlde\nJGgoUGc1R0w1VkwobXVrT3hwdS4=\n', '2014-04-05 01:51:27'), ('a9ae4c1bf89028e2f5a7e20501a9f3a6', 'ZDI5YTkxYmZkNjA3OWQ3NjgxZDEzYzk5MzE2YjJkNzY4ZDkxNDUyOTqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVCnRlc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTJhWihBRGJFTDFVbG10RkEx\nQmJnaUc5U3lHa1R4aGZKbkMwd2khYkdhN0goIVNPZGIpTlUSX2F1dGhfdXNlcl9iYWNrZW5kVSlk\namFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu\n', '2014-07-09 11:15:13'), ('ace7b31e1b6fdc6f14f209efc1d79f3a', 'NGJiMGY3NzZmODg5ZWFiNmEzMWFhZTBlMDdlMjFmMTM1MDA0MzNiMTqAAn1xAVUHY2FydF9pZHEC\nVTJkeTNJWEcmUyZ2Q1BaQUliY2JIdCk3cGNAUHNsTkZmVW1ebCY4RkRNJGowSVFpN2RHZnMu\n', '2014-04-06 15:35:50'), ('adf7cb5b28af8fe08f4014039601b3f5', 'YjYwMjk0YTM1NDVlOGViZjAwMjU1OTRjMjEyODkwMWZkMWQwMWI4YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVB2Nh\ncnRfaWRVMnNSbiZrczIlbyNYRjZwS0w4I2NNTkFUdzBieWdMRWtma1BvI2ckYUJNelJUZWNPdTg4\nVQ1fYXV0aF91c2VyX2lkigEBdS4=\n', '2014-07-11 20:43:08'), ('ae81d97b0b75cf0317d23d7e5482752f', 'MjYyNmU1M2QzMWY3ZmZkN2JlN2UzODdhMmY3MTE3ZTg1ZDVkOTBiZjqAAn1xAVUHY2FydF9pZHEC\nVTJWcnpxdUBCMEZrT3QocTR6SnIjbShsJFgpUnM0QSFkeDJYem5LNSFEeVFsWU00QXI4VXMu\n', '2014-07-23 01:00:54'), ('b3cbbecbffa08a2a78d3f53c5c388814', 'NDRjZGI4NWMyYWJkNjRjZWNhZjU1ZDUyNjZjZTlmZWQ1NjljN2EyMjqAAn1xAVUHY2FydF9pZHEC\nVTJrRSooJDJHaHkqVVJBMldmaiROdnRyVjRMNWpHbm5oWjYkRkFTbEZVI28wKElCdG9sJXMu\n', '2014-07-01 12:27:34'), ('ba900d623260c81dd11c2246db4b2c6d', 'Njg0OTViZGFiNzEyZjQxNTJmYTJkNTJkNTYxZTg3NmMzZDVjYmQwZjqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVCnRlc3Rjb29raWVVBndvcmtlZHECVQdjYXJ0X2lkVTJRalc2bHhYUVlSbDczTm5u\nNHVJZzd4Tm5pSFZ4M2hocyRUWjdzMEFMY2dsSTFNeW5qUVUSX2F1dGhfdXNlcl9iYWNrZW5kVSlk\namFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu\n', '2014-07-19 02:44:55'), ('c10f470f9d6eb046282c989710e9a2d1', 'OTVjMTY3YTE5Y2NmYzcwOTRmZDQ1YmQ3NTBlNzEzZTE0OTMwN2ZkYjqAAn1xAShVCnRlc3Rjb29r\naWVVBndvcmtlZHECVQdjYXJ0X2lkVTIobDA0MWlJaUxnSE9GZFhAbmcpcSgqdyFWQkt2eGdzNTFv\nM0paMU5kRSo0OSltTzQ0aXUu\n', '2014-07-11 16:37:33'), ('db00cc2bc18a052bec38f03d5bea3f07', 'NWE1MmM1ZjI4MTFhOGU3ZTJlYWM4ZDZiODlkYzJmZTMzZTAzNmI1MjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVDG9y\nZGVyX251bWJlcnECigEaVQlfbWVzc2FnZXNdcQMoY2RqYW5nby5jb250cmliLm1lc3NhZ2VzLnN0\nb3JhZ2UuYmFzZQpNZXNzYWdlCnEEKYFxBX1xBihVCmV4dHJhX3RhZ3NxB05VB21lc3NhZ2VxCFg9\nAAAAcHJvZHVjdCAi0JzQuNGAINCy0LDQvCIg0LHRi9C7INGD0YHQv9C10YjQvdC+INC40LfQvNC1\n0L3QtdC9LlUFbGV2ZWxxCUsUdWJoBCmBcQp9cQsoaAdYAAAAAGgIWE0AAABwcm9kdWN0ICLQmNGB\n0YbQtdC70LXQvdC40LUg0LLQtdGA0L7QuSIg0LHRi9C7INGD0YHQv9C10YjQvdC+INC40LfQvNC1\n0L3QtdC9LmgJSxR1YmVVDV9hdXRoX3VzZXJfaWSKAQFVB2NhcnRfaWRVMk9wZyhLJk9Sb3VvMlM3\nJSVpQzMkT2tQMG9EQFlCQ1paQFNUc0l4aFpjeENMUkhINFNEdS4=\n', '2014-04-05 09:43:17'), ('e3483272734a8a12b6080ccd064e172b', 'YjY0MWI4YmU2NTY5MmM2NzkzNDI0NGY4ZDRiOTVjYjBlNzIwMjk0OTqAAn1xAVUHY2FydF9pZHEC\nVTJ2eXIlRXcwaldBXm1ebSVFbihGQlolM3Q4WDBDVihyTkhwVSQjNVFwSzFkT01oRm94dHMu\n', '2014-07-14 14:28:52'), ('e6482a3bc8798220c04ac8dba1634eec', 'MWE5ODhiYWVmNmZlMDQ4MzhjYjhlM2U2ZjM1M2FjZWI2MmFlMzcxZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRVCnRl\nc3Rjb29raWVxAlUGd29ya2VkcQNVB2NhcnRfaWRVMmpIaGcpWEtDOXVkUjQ3RXc5QHEydm9mKVp4\nKG9ieilMQGE4bkV2WnphJGVZWGJMeSFGVQ1fYXV0aF91c2VyX2lkigEBdS4=\n', '2014-07-27 20:19:18'), ('eb8d17f2c64e53e6a4464daf8d6d07d9', 'MGJkODQwMDMyNDcwYjVlMDYwZGU1ODEzYWU5NDZlM2I4ZDYyM2Y0NjqAAn1xAVUHY2FydF9pZHEC\nVTIpRyRIOTlJd01MWEAoIyFTN0VNU0NjbHRwdEtoVUxCYzJSMWdoalB1N1IzUDJONGE2NnMu\n', '2014-06-27 17:09:44'), ('ee12ddc7c59809a7ac20bb6a7d0b3ad6', 'MzVlMmRjN2UyZjE4MzFhZWYyYmFkZGE2YmU3ZGViNzIxOWNmNzdjNTqAAn1xAVUHY2FydF9pZHEC\nVTJQQ1BrKVR6JTVHJWQ4OEE0dWhtV3VzQWpPUnl2aUNHZSppWE13UzJheHRUODlvTTNvXnMu\n', '2014-07-11 19:45:15'), ('f2de271bf8f8e94b42acca3ffd909ca1', 'NDgwMTYwYTMwNzc5ZGUyZTRjZGI0YmExNDllMWJiZTViOWRhZmQwMDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQdjYXJ0X2lkVTJzUVE0WClUSTlTc2g5c1NHZFdkQkUjTFlDXmc4ZDJsTVp6dHo0MTA2aEwwMGgx\nZUJBKFUNX2F1dGhfdXNlcl9pZHEEigEBdS4=\n', '2014-07-24 22:04:01'), ('f48c2603cd3b3cbdb71c7bb36385d0d5', 'NTM5YWFiYjkzM2I3N2ViODdjZjViMjVmYTk3NzhhMjg0MmNjN2M4NjqAAn1xAVUHY2FydF9pZHEC\nVTJjazhBVmM3cFZETmdNOVJpQTc3bU12d1JhbFRqWnZWMktYblJjTnI5Z3BHI0UjS3phdHMu\n', '2014-05-04 21:12:14');
COMMIT;

-- ----------------------------
--  Table structure for `django_site`
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `django_site`
-- ----------------------------
BEGIN;
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');
COMMIT;

-- ----------------------------
--  Table structure for `news`
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `header` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `views` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `news_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_1a95bf53` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Table structure for `product_images`
-- ----------------------------
DROP TABLE IF EXISTS `product_images`;
CREATE TABLE `product_images` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `description` varchar(255) NOT NULL,
  `product_id` int(11) NOT NULL,
  `default` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_images_bb420c12` (`product_id`),
  CONSTRAINT `product_id_refs_id_f2acfb67` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `product_images`
-- ----------------------------
BEGIN;
INSERT INTO `product_images` VALUES ('17', 'products/images/DSC_2005_1.jpg', '', '11', '1'), ('18', 'products/images/DSC_2007_1.jpg', '', '11', '0'), ('19', 'products/images/DSC_2008_1.jpg', '', '11', '0'), ('20', 'products/images/IMG_4952.JPG', '', '12', '1'), ('21', 'products/images/IMG_4953.JPG', '', '12', '0'), ('22', 'products/images/IMG_4954.JPG', '', '12', '0'), ('23', 'products/images/IMG_4960.JPG', '', '13', '1'), ('24', 'products/images/IMG_4956.JPG', '', '13', '0'), ('25', 'products/images/IMG_4958.JPG', '', '13', '0'), ('26', 'products/images/DSC_0285.jpg', '', '13', '0'), ('27', 'products/images/DSC_0255.jpg', '', '12', '0'), ('28', 'products/images/DSC_0258.jpg', '', '12', '0'), ('29', 'products/images/DSC_0247.jpg', '', '12', '0'), ('30', 'products/images/DSC_0295.jpg', '', '12', '0');
COMMIT;

-- ----------------------------
--  Table structure for `products`
-- ----------------------------
DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(255) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `sku` varchar(50) NOT NULL,
  `price` decimal(9,2) NOT NULL,
  `old_price` decimal(9,2) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_bestseller` tinyint(1) NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `quantity` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `meta_keywords` varchar(255) NOT NULL,
  `meta_description` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `articul` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `products`
-- ----------------------------
BEGIN;
INSERT INTO `products` VALUES ('11', 'Очки', 'ochki', '', '', '1111.00', '0.00', '1', '1', '1', '22', 'Description', '', '', '2014-04-20 02:39:21', '2014-04-20 02:39:30', ''), ('12', 'Крестик', 'krestik', 'Производитель \"Церковь Прославления\"  г.Томск', '', '123.00', '0.00', '1', '1', '1', '21', 'В книге приведены анализ и места из Библии порядка 100000 примеров проявлений 1000 состояний сознания человека, половина которых – грех и зло, а другая святость и добро. Назначение книги - послужить читателю простым и доступным путеводителем по текстам Библии о совести и сознании.', '', '', '2014-04-23 09:20:06', '2014-04-26 12:35:04', ''), ('13', 'Еще крестик', 'eshe-krestik', 'Производитель крестика \"Слово Жизни\" г.Москва', '', '3123.00', '0.00', '1', '1', '1', '21', 'В книге приведены анализ и места из Библии порядка 100000 примеров проявлений 1000 состояний сознания человека, половина которых – грех и зло, а другая святость и добро. Назначение книги - послужить читателю простым и доступным путеводителем по текстам Библии о совести и сознании.', '', '', '2014-04-23 09:22:27', '2014-04-26 12:31:53', '');
COMMIT;

-- ----------------------------
--  Table structure for `products_categories`
-- ----------------------------
DROP TABLE IF EXISTS `products_categories`;
CREATE TABLE `products_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`,`category_id`),
  KEY `products_categories_bb420c12` (`product_id`),
  KEY `products_categories_42dc49bc` (`category_id`),
  CONSTRAINT `category_id_refs_id_caa5a09f` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `product_id_refs_id_7a5f8ca1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `products_categories`
-- ----------------------------
BEGIN;
INSERT INTO `products_categories` VALUES ('41', '11', '30'), ('50', '12', '34'), ('49', '13', '34');
COMMIT;

-- ----------------------------
--  Table structure for `search_terms`
-- ----------------------------
DROP TABLE IF EXISTS `search_terms`;
CREATE TABLE `search_terms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `query` varchar(50) NOT NULL,
  `search_date` datetime NOT NULL,
  `ip_address` char(15) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `search_terms_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_f0816fd4` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `search_terms`
-- ----------------------------
BEGIN;
INSERT INTO `search_terms` VALUES ('1', 'книги', '2014-01-03 23:15:28', '127.0.0.1', '1'), ('2', 'book', '2014-01-03 23:15:51', '127.0.0.1', '1'), ('3', 'book', '2014-01-03 23:16:02', '127.0.0.1', '1'), ('4', 'книг', '2014-01-03 23:16:10', '127.0.0.1', '1'), ('5', 'библия', '2014-01-04 20:57:49', '127.0.0.1', '1');
COMMIT;

-- ----------------------------
--  Table structure for `slider_slider`
-- ----------------------------
DROP TABLE IF EXISTS `slider_slider`;
CREATE TABLE `slider_slider` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `slider_slider_bb420c12` (`product_id`),
  CONSTRAINT `product_id_refs_id_2e076718898d693` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `slider_slider`
-- ----------------------------
BEGIN;
INSERT INTO `slider_slider` VALUES ('1', 'slider/bg-slide0.jpg', '12'), ('2', 'slider/bg-slide2.jpg', '13');
COMMIT;

-- ----------------------------
--  Table structure for `south_migrationhistory`
-- ----------------------------
DROP TABLE IF EXISTS `south_migrationhistory`;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `south_migrationhistory`
-- ----------------------------
BEGIN;
INSERT INTO `south_migrationhistory` VALUES ('1', 'catalog', '0001_initial', '2014-03-31 01:17:53'), ('2', 'checkout', '0001_initial', '2014-04-09 15:01:11'), ('3', 'checkout', '0002_auto__del_field_orderoneclick_product', '2014-04-09 17:22:38'), ('4', 'checkout', '0003_auto__add_field_orderoneclick_product', '2014-04-09 17:43:15'), ('5', 'checkout', '0004_auto__del_field_orderoneclick_product', '2014-04-09 20:56:05'), ('6', 'checkout', '0005_auto__add_field_orderoneclick_product_name', '2014-04-09 20:57:54'), ('7', 'dashboard', '0001_initial', '2014-04-10 21:16:52'), ('8', 'dashboard', '0002_auto__add_field_dashboardpreferences_dashboard_id', '2014-04-10 21:16:52'), ('9', 'dashboard', '0003_auto__add_unique_dashboardpreferences_dashboard_id_user', '2014-04-10 21:16:52'), ('10', 'menu', '0001_initial', '2014-04-10 21:17:02'), ('11', 'checkout', '0006_auto__del_field_order_shipping_zip', '2014-04-12 20:07:14'), ('12', 'checkout', '0007_auto__del_field_order_shipping_address_2__del_field_order_shipping_cou', '2014-04-12 20:10:56'), ('13', 'catalog', '0002_auto__add_field_product_articul', '2014-04-13 01:45:15'), ('14', 'slider', '0001_initial', '2014-04-23 09:06:08');
COMMIT;

-- ----------------------------
--  Table structure for `thumbnail_kvstore`
-- ----------------------------
DROP TABLE IF EXISTS `thumbnail_kvstore`;
CREATE TABLE `thumbnail_kvstore` (
  `key` varchar(200) NOT NULL,
  `value` longtext NOT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

-- ----------------------------
--  Records of `thumbnail_kvstore`
-- ----------------------------
BEGIN;
INSERT INTO `thumbnail_kvstore` VALUES ('sorl-thumbnail||image||01baad2309eab22a7dfc2392b970ac28', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/af/7b/af7b9846202258152f3cbf7989bf38d6.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||04908a620f7f59e72bd6f853ded87a7d', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/d9/07/d907f3b46e199978be4142a5de25a647.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||0525a515f0ff69a29911eba31d3c1800', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/97/7e/977e1883adbe098999a27d0f758750e6.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||058f32560a6d4a3df28d0071d0ab4692', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/c0/41/c0419de3834994ed45efecf3a03db343.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||060215279d4577ffe83fd9a8b4cf0619', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/6c/e4/6ce4efe46fdf9ef153510882e20a4a0d.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||094f5bd4b068f677dc999f6d2a047099', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/04/c0/04c0a30fed9195049b11f9987c5d7829.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||0a42ecf5cb98ecd2f5086d5d78658be0', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/5e/9e/5e9eebecf149d03f26f61c2c25ea2d51.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||0c95fe303f03c5442c44bbcdfefe5b75', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/f0/ab/f0abeb766a8d861ff5874f0765b4438a.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||0efaef32a7cff0156ea77b7caf005a89', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/62/b5/62b5d5864feae105d663828efaf99672.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||0fd5b8c4aed80e133761e4c455e63788', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/ba/48/ba4862cfacc3df02bb69cb861899b656.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||118920442cc062a882af75fb151dd04e', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/b1/a6/b1a6ccbfb94364c3dd8bff4b2dc173c7.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||139a39db4786df21e6e53db9bf921e39', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/c7/c2/c7c2117f8a1bf5ab6a68cd9f614c7b0b.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||1bd7e12d83288d76ed14b74ae0732e52', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/37/32/3732e41628aca5c20e191f3a67622153.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||1c9f1a47c4c3d07f03a318849d33bb3a', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/82/3a/823abe2bae11b934536bce34809fa393.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||1d28be5dabc0e43250bcc837ad412659', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4960.JPG\", \"size\": [1024, 683]}'), ('sorl-thumbnail||image||1e7dd78b3ce25097ff208b4d7cba0349', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/06/3f/063f7c5f86a1a461379a90928d482f4e.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||1ee5bea6e332cbfb9b4f2cd9f632c390', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/18/46/18462be7566b9b3706fc2a1d12c1e99d.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||24040201c489c717b32c290d8a8c135b', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/b0/e4/b0e4e7da5c5a184e03125ff47654cfa8.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||24c47fca199e2f567fd3c2e67777707b', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/2c/52/2c525455017b643199d0fc79098b8a3f.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||279775c626bf55a2f7cc6ce11b02c774', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/0b/6f/0b6f32453a4e64a0a65644bf074e72d9.jpg\", \"size\": [198, 219]}'), ('sorl-thumbnail||image||29701fcb1df3463240604d34e43fed11', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4953.JPG\", \"size\": [1024, 683]}'), ('sorl-thumbnail||image||2a695b145acf5642c307c909bbfb86bc', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/e8/4c/e84ce1082433027e1a052b408343ad03.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||31512980246628590c634e0d46ad90fe', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/2a/9b/2a9bdc878d6f7e66f143a1164bbcb883.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||35cb39bcf65fe36a362c9d0b92f7a5bf', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/db/90/db90834374f517b76d2100b57c72d4f9.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||35db70787ffed4d0ccdef5ec21d596f1', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/f7/41/f74150550f2025087fab28b71b4210ea.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||36c3f12284f6641336dfce3ce79ce77b', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/b1/10/b110141329254e2f5048fdb43f302a9f.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||381b50f2641d73423f8ebc9238bbcfa3', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg6-product_5.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||3c7824bd96a54eada884902d28d47631', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg10-product_5.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||3ef4689634f7a2ba6be4d1c0985fceb5', '{\"storage\": \"sorl.thumbnail.images.UrlStorage\", \"name\": \"http://127.0.0.1:8000/media/products/images/handbags_2.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||3ffff115980b8af1f40616414afdc42e', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4954.JPG\", \"size\": [1024, 683]}'), ('sorl-thumbnail||image||4655ccae31bafa0ea1d073aecefc5c43', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_0255.jpg\", \"size\": [900, 599]}'), ('sorl-thumbnail||image||46bb5c21f2ffc14b1dd1ca2b7a0e74d3', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4958.JPG\", \"size\": [1024, 1536]}'), ('sorl-thumbnail||image||4731d3a960812e931307c95a526cbbb8', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/5f/c6/5fc66528b0d76c6e549f0c1c83818c7d.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||4f3fe496528d05b0fd696be69a80dcaf', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/e6/a4/e6a4a3b52feaa8a9fda0306557031e8f.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||52d09073d9650602af4d46a64a7db0ff', '{\"storage\": \"sorl.thumbnail.images.UrlStorage\", \"name\": \"http://127.0.0.1:8000/static/images/odejda.jpg\", \"size\": [390, 304]}'), ('sorl-thumbnail||image||582b302c2603f4af776484fcb606cd46', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/b4/82/b4829964f7f75c614ec6c6aba438e9ee.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||5ad0d95f8c64ee77b5739d687cd40ee3', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/7f/69/7f69336a4d6effa4c1bb3978afed233e.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||5bd78aec4d84973c3871deb53e7ec23f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/cc/4b/cc4b8750500446ef8dbfb3a423ddd416.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||5fb8b8daf3a43d3065384c1fbb78315d', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/57/13/5713143dcc1aa5706ee2177e6b01fce0.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||610b9abbff4ab1f273d186e9d1ad6233', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg3-product_4.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||6324d0dcd28364aeb2dabbca9ccb3257', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/03/b2/03b231fab7e2dfa03aab7b851e5fb3f8.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||633ea7810441d8c416019db7fce1dc41', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg12-product_2_1.jpg\", \"size\": [650, 650]}'), ('sorl-thumbnail||image||638f07a4fc5dda67e65a9c47473ec493', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/f0/5b/f05b457f842e211d85179a460b017eea.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||64c39342e3faa6a29b36375dcbc704c8', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/54/ef/54ef66359f2b5d826e617b0f6acc2352.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||68aa97108d1b1c990bba87cd8c5fec17', '{\"storage\": \"sorl.thumbnail.images.UrlStorage\", \"name\": \"http://hashcode.ru/upfiles/logo.png\", \"size\": [240, 70]}'), ('sorl-thumbnail||image||7248cbb1a78cb941d1566d48563c14d0', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/88/31/8831b8ed0ee8ec15ea489620ce5dd143.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||736b1e3c3dba63d88bc38972349961f6', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/ba/d4/bad42bdcd6664d5173072b046a2cf6a1.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||7888430ff0551bef014bfc0140f1e7d6', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/4c/53/4c53dede78b53530cdb68e40fb6d63d2.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||79ba069a5a93e53003209ee5b4961631', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_0285.jpg\", \"size\": [900, 599]}'), ('sorl-thumbnail||image||7a0c80ef33a70a5b3eae08539437901f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/30/bd/30bd2b84646be6bfbcdaee965026e3d6.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||7ce972a861d4f14c03cdd2841d75b621', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/3d/89/3d8920c2e12de70f86d826ed71475433.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||7dd57adaa039fbd8116ac4a3a590800a', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/d5/75/d575f2a399c6dc0800073374578b0a81.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||83d66ec99f11a32163feadc2149efcc0', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4952.JPG\", \"size\": [1024, 683]}'), ('sorl-thumbnail||image||865b0a8c0aca7371cdcf13a37a24399d', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/50/40/5040f2385c41aa5cbd8d3e2a65bbb0c9.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||87576670258fb5e0fe3cc60b78b1fd11', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/dd/17/dd1717f2db3dfb80d3882e47415f1920.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||8975f19ff27b152bf071724937a5a1f8', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/handbags_2.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||8996736a769d7e34cca0e9bb4bdcd48f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/06/7f/067f4905db7b59736d66d17dfc157cba.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||8a2764d985abc4eed7e2ab2c335d37ad', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/130971_0.jpg\", \"size\": [224, 168]}'), ('sorl-thumbnail||image||8c7f787493211a929b1627ba22c0d1d5', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/IMG_4956.JPG\", \"size\": [1024, 1536]}'), ('sorl-thumbnail||image||8f48f428be7acfddda744f29638ecffe', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/4b/6a/4b6abf14637c87f2bae69825541be941.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||9670541e3aff6e369d5e636ea5f49838', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/07/9e/079e2240b297e611a1761daaad0f976b.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||99f8f0d320a2a62e83b575aa8b8657e6', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_2005_1.jpg\", \"size\": [1200, 795]}'), ('sorl-thumbnail||image||a2245bce54a8b99092a60bfb36408585', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_0295.jpg\", \"size\": [900, 599]}'), ('sorl-thumbnail||image||a462ae34c2f3dd34e386769882690225', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg7-product_4_1.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||a4b238da0fbb8ba9783fbe01737ebaca', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/05/98/0598c4110a7672f2eeb8a762dc9efe6f.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||aa563f394552a83133a6a875eef8edfa', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg11-product_2.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||abfdf2241849d55d7409869f6360cb2c', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/29/38/2938207efb1e81734dc983f52b16cce0.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||b6c9b8e8f5202d94105081bdd6f1682c', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/0c/6c/0c6ccff7f5ad855c0f826df4d86440a8.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||b7698457e4a6e4e671d63b43545fae8e', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_2008_1.jpg\", \"size\": [1200, 795]}'), ('sorl-thumbnail||image||b926948f57192b5bc7da135e4a69470f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg3-product_4_1.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||b9ca44f579f13da039b8270de4f93e3f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/fd/a8/fda84ab014e752cecd86e4d098fdb176.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||bb31417ddfb098b51390046a9e4436a5', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/69/e1/69e133c560433de2cd0b52ee2af9f48c.jpg\", \"size\": [255, 255]}'), ('sorl-thumbnail||image||bd377d6afbfb523c882f7ad801e385b8', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/24/5f/245f61d817ec772bd94cab5057011adc.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||c1a28ca27cc3464b80181b7fa373e177', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/80/98/8098ed0e48ffd463ba4fe4b4817784c6.jpg\", \"size\": [360, 360]}'), ('sorl-thumbnail||image||c3489888197c91ef42490881b957e152', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/21/31/2131cfe25627e07875c360dcfe45a368.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||ca65eae9f8fd29eb90a34c8f7341b3cd', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/112510_0.1329449314.jpg\", \"size\": [168, 224]}'), ('sorl-thumbnail||image||ca92b6282e0d6fca1459c450ed047b2d', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/ff/a3/ffa35651a6c2844436873950cbc26f7b.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||cf4371db1e4e17f1b5d47c8b553048ec', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/63/09/630952d905a5bed542d47b11c71d4763.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||d5677f66cb3c28671692a0c87e220e03', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/4f/74/4f740aba47d514bdce38d8b2e694be60.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||d71ea6aade10926346ba1429bea0488e', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/fc/04/fc040af8de8f9fb53f6dcb366623188b.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||d90735f1d9b731a527771d9db3433055', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/96/15/96155242f3176d17c6cd5a56c2d148c8.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||e38fadde4bc6861c33549bd2ccb4fd98', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/ed/3f/ed3f417c0368f7c60e90b04e55498a1a.jpg\", \"size\": [100, 100]}'), ('sorl-thumbnail||image||e77604d894108d26fb08d18be706cfa6', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/d8/08/d80885c619be90d80ff96f28f3318dec.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||e7ff298c4ba693e4df387a18a69656a1', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_0258.jpg\", \"size\": [900, 599]}'), ('sorl-thumbnail||image||e98904a87d561258a4c822454c92d243', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/1e/6f/1e6f88e077359f48df7336a4b17a1cb7.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||e9fc807e07ea1e7a7990792a3baf70f9', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/56/e6/56e6aab46952fbca0c4b9d96ccc28483.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||f4ca958e267a6e48f0813ce270269224', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/4f/ac/4facb2e1e2025a33831ee69479b48ebb.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||f53c80c1e5dda38054ff8a407d2ee57c', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_2007_1.jpg\", \"size\": [1200, 795]}'), ('sorl-thumbnail||image||f677286d6da21089f8f36e89ce936dcb', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/DSC_0247.jpg\", \"size\": [900, 599]}'), ('sorl-thumbnail||image||f7054b60c36446403a28aeb1e085e782', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/85/50/85501f414ef49327d18f1a5f49534c70.jpg\", \"size\": [200, 200]}'), ('sorl-thumbnail||image||fb4073cd6cc76d4cf67d2e0b32d9f28f', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg7-product_4_2.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||image||fc1cf15e91adbc89c94fe571b4ef45a3', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"cache/a2/bd/a2bde05cee9836c6f0d679e1d63053fc.jpg\", \"size\": [298, 319]}'), ('sorl-thumbnail||image||fc6d02c8dfd75c5a5a836e9a8ec203eb', '{\"storage\": \"django.core.files.storage.FileSystemStorage\", \"name\": \"products/images/bg11-product_2_1.jpg\", \"size\": [1200, 1200]}'), ('sorl-thumbnail||thumbnails||1d28be5dabc0e43250bcc837ad412659', '[\"e77604d894108d26fb08d18be706cfa6\", \"7248cbb1a78cb941d1566d48563c14d0\", \"c3489888197c91ef42490881b957e152\", \"7a0c80ef33a70a5b3eae08539437901f\"]'), ('sorl-thumbnail||thumbnails||29701fcb1df3463240604d34e43fed11', '[\"d71ea6aade10926346ba1429bea0488e\", \"7888430ff0551bef014bfc0140f1e7d6\"]'), ('sorl-thumbnail||thumbnails||381b50f2641d73423f8ebc9238bbcfa3', '[\"9670541e3aff6e369d5e636ea5f49838\", \"279775c626bf55a2f7cc6ce11b02c774\", \"a4b238da0fbb8ba9783fbe01737ebaca\", \"139a39db4786df21e6e53db9bf921e39\"]'), ('sorl-thumbnail||thumbnails||3c7824bd96a54eada884902d28d47631', '[\"8996736a769d7e34cca0e9bb4bdcd48f\", \"bb31417ddfb098b51390046a9e4436a5\"]'), ('sorl-thumbnail||thumbnails||3ef4689634f7a2ba6be4d1c0985fceb5', '[\"cf4371db1e4e17f1b5d47c8b553048ec\"]'), ('sorl-thumbnail||thumbnails||3ffff115980b8af1f40616414afdc42e', '[\"7ce972a861d4f14c03cdd2841d75b621\", \"bd377d6afbfb523c882f7ad801e385b8\"]'), ('sorl-thumbnail||thumbnails||4655ccae31bafa0ea1d073aecefc5c43', '[\"5ad0d95f8c64ee77b5739d687cd40ee3\", \"1c9f1a47c4c3d07f03a318849d33bb3a\"]'), ('sorl-thumbnail||thumbnails||46bb5c21f2ffc14b1dd1ca2b7a0e74d3', '[\"d90735f1d9b731a527771d9db3433055\", \"5fb8b8daf3a43d3065384c1fbb78315d\"]'), ('sorl-thumbnail||thumbnails||52d09073d9650602af4d46a64a7db0ff', '[\"ca92b6282e0d6fca1459c450ed047b2d\"]'), ('sorl-thumbnail||thumbnails||610b9abbff4ab1f273d186e9d1ad6233', '[\"1e7dd78b3ce25097ff208b4d7cba0349\", \"0fd5b8c4aed80e133761e4c455e63788\"]'), ('sorl-thumbnail||thumbnails||633ea7810441d8c416019db7fce1dc41', '[\"582b302c2603f4af776484fcb606cd46\", \"4731d3a960812e931307c95a526cbbb8\", \"736b1e3c3dba63d88bc38972349961f6\"]'), ('sorl-thumbnail||thumbnails||68aa97108d1b1c990bba87cd8c5fec17', '[\"36c3f12284f6641336dfce3ce79ce77b\"]'), ('sorl-thumbnail||thumbnails||79ba069a5a93e53003209ee5b4961631', '[\"865b0a8c0aca7371cdcf13a37a24399d\", \"0525a515f0ff69a29911eba31d3c1800\"]'), ('sorl-thumbnail||thumbnails||83d66ec99f11a32163feadc2149efcc0', '[\"1bd7e12d83288d76ed14b74ae0732e52\", \"abfdf2241849d55d7409869f6360cb2c\", \"d5677f66cb3c28671692a0c87e220e03\", \"1ee5bea6e332cbfb9b4f2cd9f632c390\"]'), ('sorl-thumbnail||thumbnails||8975f19ff27b152bf071724937a5a1f8', '[\"c1a28ca27cc3464b80181b7fa373e177\", \"058f32560a6d4a3df28d0071d0ab4692\", \"2a695b145acf5642c307c909bbfb86bc\"]'), ('sorl-thumbnail||thumbnails||8a2764d985abc4eed7e2ab2c335d37ad', '[\"094f5bd4b068f677dc999f6d2a047099\"]'), ('sorl-thumbnail||thumbnails||8c7f787493211a929b1627ba22c0d1d5', '[\"e98904a87d561258a4c822454c92d243\", \"24040201c489c717b32c290d8a8c135b\"]'), ('sorl-thumbnail||thumbnails||99f8f0d320a2a62e83b575aa8b8657e6', '[\"f7054b60c36446403a28aeb1e085e782\", \"0efaef32a7cff0156ea77b7caf005a89\", \"e38fadde4bc6861c33549bd2ccb4fd98\", \"04908a620f7f59e72bd6f853ded87a7d\"]'), ('sorl-thumbnail||thumbnails||a2245bce54a8b99092a60bfb36408585', '[\"060215279d4577ffe83fd9a8b4cf0619\", \"7dd57adaa039fbd8116ac4a3a590800a\"]'), ('sorl-thumbnail||thumbnails||a462ae34c2f3dd34e386769882690225', '[\"f4ca958e267a6e48f0813ce270269224\", \"b9ca44f579f13da039b8270de4f93e3f\", \"24c47fca199e2f567fd3c2e67777707b\"]'), ('sorl-thumbnail||thumbnails||aa563f394552a83133a6a875eef8edfa', '[\"6324d0dcd28364aeb2dabbca9ccb3257\", \"fc1cf15e91adbc89c94fe571b4ef45a3\"]'), ('sorl-thumbnail||thumbnails||b7698457e4a6e4e671d63b43545fae8e', '[\"35db70787ffed4d0ccdef5ec21d596f1\", \"638f07a4fc5dda67e65a9c47473ec493\"]'), ('sorl-thumbnail||thumbnails||b926948f57192b5bc7da135e4a69470f', '[\"01baad2309eab22a7dfc2392b970ac28\", \"0a42ecf5cb98ecd2f5086d5d78658be0\"]'), ('sorl-thumbnail||thumbnails||ca65eae9f8fd29eb90a34c8f7341b3cd', '[\"e9fc807e07ea1e7a7990792a3baf70f9\"]'), ('sorl-thumbnail||thumbnails||e7ff298c4ba693e4df387a18a69656a1', '[\"b6c9b8e8f5202d94105081bdd6f1682c\", \"64c39342e3faa6a29b36375dcbc704c8\"]'), ('sorl-thumbnail||thumbnails||f53c80c1e5dda38054ff8a407d2ee57c', '[\"5bd78aec4d84973c3871deb53e7ec23f\", \"0c95fe303f03c5442c44bbcdfefe5b75\"]'), ('sorl-thumbnail||thumbnails||f677286d6da21089f8f36e89ce936dcb', '[\"35cb39bcf65fe36a362c9d0b92f7a5bf\", \"118920442cc062a882af75fb151dd04e\"]'), ('sorl-thumbnail||thumbnails||fb4073cd6cc76d4cf67d2e0b32d9f28f', '[\"4f3fe496528d05b0fd696be69a80dcaf\", \"8f48f428be7acfddda744f29638ecffe\"]'), ('sorl-thumbnail||thumbnails||fc6d02c8dfd75c5a5a836e9a8ec203eb', '[\"31512980246628590c634e0d46ad90fe\", \"87576670258fb5e0fe3cc60b78b1fd11\"]');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
