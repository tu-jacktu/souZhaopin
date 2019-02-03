CREATE TABLE `city_code` (
  `city_id` varchar(5) NOT NULL,
  `city_name` varchar(255) NOT NULL,
  `city_area` double(10,2) DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

CREATE TABLE `job_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sou_city_id` varchar(5) DEFAULT NULL,
  `page_index` int(11) DEFAULT NULL,
  `detail` text,
  `updateDate` varchar(255) DEFAULT NULL,
  `city_display` varchar(255) DEFAULT NULL,
  `endDate` varchar(255) DEFAULT NULL,
  `positionURL` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `number` varchar(255) DEFAULT NULL,
  `vipLevel` varchar(255) DEFAULT NULL,
  `workingExp_name` varchar(255) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `company_type_name` varchar(255) DEFAULT NULL,
  `company_url` varchar(255) DEFAULT NULL,
  `createDate` varchar(255) DEFAULT NULL,
  `jobName` varchar(255) DEFAULT NULL,
  `eduLevel_name` varchar(255) DEFAULT NULL,
  `eduLevel_code` varchar(255) DEFAULT NULL,
  `emplType` varchar(255) DEFAULT NULL,
  `timeState` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=811 DEFAULT CHARSET=utf8 ;