-- Create table
create table SD_T_DAIBIAOXINXI
(
  id                             VARCHAR2(32) default sys_guid() not null,
  code                           VARCHAR2(10),
  name                           VARCHAR2(50),
  fullname                       VARCHAR2(50),
  pro_name                       VARCHAR2(10),
  city_name                      VARCHAR2(10),
  county_name                    VARCHAR2(10),
  city_division                  VARCHAR2(20),
  county_division                VARCHAR2(20),
  relationship                   VARCHAR2(20),
  sr_states                      VARCHAR2(8),
  person_name                    VARCHAR2(50),
  person_id                      VARCHAR2(20),
  address                        VARCHAR2(300),
  ems_code                       VARCHAR2(30),
  phone                          VARCHAR2(100),
  send_pattern                   VARCHAR2(20),
  out_min_money                  NUMBER,
  transfer_min_money             NUMBER,
  auto_collection                VARCHAR2(10),
  channel_1                      VARCHAR2(20),
  channel_2                      VARCHAR2(20),
  channel_3                      VARCHAR2(20),
  distribution_1                 VARCHAR2(20),
  distribution_2                 VARCHAR2(20),
  distribution_3                 VARCHAR2(20),
  order_warehouse                VARCHAR2(20),
  refund_ticket_permit           VARCHAR2(10),
  submit_order_permit            VARCHAR2(10),
  order_automatic_permit         VARCHAR2(10),
  sale_commission_proportion     NUMBER,
  sale_commission_modul          VARCHAR2(20),
  sale_commission_pay            VARCHAR2(10),
  duijiang_commission_proportion NUMBER,
  duijiang_commission_modul      VARCHAR2(20),
  duijiang_commission_way        VARCHAR2(10),
  duijiang_commission_pay        VARCHAR2(20),
  manage_commission_proportion   NUMBER,
  manage_commission_modul        VARCHAR2(20),
  manage_commission_way          VARCHAR2(10),
  manage_commission_pay          VARCHAR2(20),
  duijiang_max_money             NUMBER,
  duijiang_min_money             NUMBER,
  duijiang_pay_sure_money        NUMBER,
  cycle                          NUMBER,
  duijiang_times                 NUMBER,
  clock_time                     VARCHAR2(10),
  transfer_out_permit            VARCHAR2(10),
  transfer_in_permit             VARCHAR2(10),
  receive_person                 VARCHAR2(50),
  receive_address                VARCHAR2(300),
  receive_phone                  VARCHAR2(100),
  manage_date                    VARCHAR2(10)
)
tablespace SPORTS_LOTTERY_DATA
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
-- Add comments to the table 
comment on table SD_T_DAIBIAOXINXI
  is 'ɽ�� �������� - ���۴�����Ϣ �ŵ�����';
-- Add comments to the columns 
comment on column SD_T_DAIBIAOXINXI.code
  is 'SR���';
comment on column SD_T_DAIBIAOXINXI.name
  is 'SR����';
comment on column SD_T_DAIBIAOXINXI.fullname
  is 'SRȫ��';
comment on column SD_T_DAIBIAOXINXI.pro_name
  is 'ʡ����';
comment on column SD_T_DAIBIAOXINXI.city_name
  is '������';
comment on column SD_T_DAIBIAOXINXI.county_name
  is '������';
comment on column SD_T_DAIBIAOXINXI.city_division
  is '������';
comment on column SD_T_DAIBIAOXINXI.county_division
  is '������';
comment on column SD_T_DAIBIAOXINXI.relationship
  is '������ϵ';
comment on column SD_T_DAIBIAOXINXI.sr_states
  is 'SR״̬';
comment on column SD_T_DAIBIAOXINXI.person_name
  is 'ҵ������';
comment on column SD_T_DAIBIAOXINXI.person_id
  is 'ҵ��֤����';
comment on column SD_T_DAIBIAOXINXI.address
  is '��ϵ��ַ';
comment on column SD_T_DAIBIAOXINXI.ems_code
  is '��������';
comment on column SD_T_DAIBIAOXINXI.phone
  is '��ϵ��ʽ';
comment on column SD_T_DAIBIAOXINXI.send_pattern
  is '�ַ�ģʽ';
comment on column SD_T_DAIBIAOXINXI.out_min_money
  is 'ת�����׽��';
comment on column SD_T_DAIBIAOXINXI.transfer_min_money
  is 'ת�˱��׽��';
comment on column SD_T_DAIBIAOXINXI.auto_collection
  is '�Զ��鼯';
comment on column SD_T_DAIBIAOXINXI.channel_1
  is '��������1';
comment on column SD_T_DAIBIAOXINXI.channel_2
  is '��������2';
comment on column SD_T_DAIBIAOXINXI.channel_3
  is '��������3';
comment on column SD_T_DAIBIAOXINXI.distribution_1
  is '����SR1';
comment on column SD_T_DAIBIAOXINXI.distribution_2
  is '����SR2';
comment on column SD_T_DAIBIAOXINXI.distribution_3
  is '����SR3';
comment on column SD_T_DAIBIAOXINXI.order_warehouse
  is '�����ֿ�';
comment on column SD_T_DAIBIAOXINXI.refund_ticket_permit
  is '����Ʊ���';
comment on column SD_T_DAIBIAOXINXI.submit_order_permit
  is '�����ύ���';
comment on column SD_T_DAIBIAOXINXI.order_automatic_permit
  is '�����Զ��������';
comment on column SD_T_DAIBIAOXINXI.sale_commission_proportion
  is '����Ӷ�����';
comment on column SD_T_DAIBIAOXINXI.sale_commission_modul
  is '����Ӷ��ģʽ';
comment on column SD_T_DAIBIAOXINXI.sale_commission_pay
  is '����Ӷ��ֵ֧����ʽ';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_proportion
  is '�ҽ�Ӷ�����';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_modul
  is '�ҽ�Ӷ��ģʽ';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_way
  is '�ҽ�Ӷ��������';
comment on column SD_T_DAIBIAOXINXI.duijiang_commission_pay
  is '�ҽ�Ӷ��֧����ʽ';
comment on column SD_T_DAIBIAOXINXI.manage_commission_proportion
  is '����Ӷ�����';
comment on column SD_T_DAIBIAOXINXI.manage_commission_modul
  is '����Ӷ��ģʽ';
comment on column SD_T_DAIBIAOXINXI.manage_commission_way
  is '����Ӷ��������';
comment on column SD_T_DAIBIAOXINXI.manage_commission_pay
  is '����Ӷ���ƶȷ�ʽ';
comment on column SD_T_DAIBIAOXINXI.duijiang_max_money
  is '�ҽ�����޶�';
comment on column SD_T_DAIBIAOXINXI.duijiang_min_money
  is '�ҽ�����޶�';
comment on column SD_T_DAIBIAOXINXI.duijiang_pay_sure_money
  is '�ҽ�֧��ȷ�Ͻ��';
comment on column SD_T_DAIBIAOXINXI.cycle
  is '����';
comment on column SD_T_DAIBIAOXINXI.duijiang_times
  is '�ҽ�����';
comment on column SD_T_DAIBIAOXINXI.clock_time
  is '����ʱ��';
comment on column SD_T_DAIBIAOXINXI.transfer_out_permit
  is 'ת��ת�����';
comment on column SD_T_DAIBIAOXINXI.transfer_in_permit
  is 'ת��ת�����';
comment on column SD_T_DAIBIAOXINXI.receive_person
  is '�����ջ���';
comment on column SD_T_DAIBIAOXINXI.receive_address
  is '�����ջ���ַ';
comment on column SD_T_DAIBIAOXINXI.receive_phone
  is '���͵绰���ջ��˵绰��';
comment on column SD_T_DAIBIAOXINXI.manage_date
  is '����';
-- Create/Recreate primary, unique and foreign key constraints 
alter table SD_T_DAIBIAOXINXI
  add constraint SD_T_DAIBIAOXINXI_PK primary key (ID)
  using index 
  tablespace SPORTS_LOTTERY_DATA
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
