-- Create table
create table SD_T_MENDIANXINXI
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
  business_type                  VARCHAR2(20),
  site_states                    VARCHAR2(8),
  person_name                    VARCHAR2(50),
  person_id                      VARCHAR2(20),
  address                        VARCHAR2(300),
  phone                          VARCHAR2(100),
  ems_code                       VARCHAR2(30),
  out_min_money                  NUMBER,
  transfer_min_money             NUMBER,
  relationship                   VARCHAR2(20),
  site_level                     VARCHAR2(10),
  channel_1                      VARCHAR2(20),
  channel_2                      VARCHAR2(20),
  channel_3                      VARCHAR2(20),
  send_pattern                   VARCHAR2(20),
  manage_sr                      VARCHAR2(50),
  move_sr1                       VARCHAR2(20),
  move_sr2                       VARCHAR2(20),
  move_sr3                       VARCHAR2(20),
  distribution_1                 VARCHAR2(20),
  distribution_2                 VARCHAR2(20),
  distribution_3                 VARCHAR2(20),
  order_warehouse                VARCHAR2(20),
  refund_ticket_permit           VARCHAR2(10),
  submit_order_permit            VARCHAR2(10),
  sure_active_mony               VARCHAR2(10),
  manual_activation_permit       VARCHAR2(10),
  order_automatic_permit         VARCHAR2(10),
  sale_commission_proportion     NUMBER,
  sale_commission_modul          VARCHAR2(20),
  sale_commission_way            VARCHAR2(10),
  sale_commission_pay            VARCHAR2(20),
  duijiang_commission_proportion NUMBER,
  duijiang_commission_modul      VARCHAR2(20),
  duijiang_commission_way        VARCHAR2(10),
  duijiang_commission_pay        VARCHAR2(20),
  duijiang_max_money             NUMBER,
  duijiang_min_money             NUMBER,
  duijiang_pay_sure_money        NUMBER,
  cycle                          NUMBER,
  duijiang_times                 NUMBER,
  clock_time                     VARCHAR2(10),
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
comment on table SD_T_MENDIANXINXI
  is 'ɽ�� �������� - �ŵ���Ϣ �ŵ�����';
-- Add comments to the columns 
comment on column SD_T_MENDIANXINXI.code
  is '�ŵ���';
comment on column SD_T_MENDIANXINXI.name
  is '�ŵ�����';
comment on column SD_T_MENDIANXINXI.fullname
  is '�ŵ�ȫ��';
comment on column SD_T_MENDIANXINXI.pro_name
  is 'ʡ����';
comment on column SD_T_MENDIANXINXI.city_name
  is '������';
comment on column SD_T_MENDIANXINXI.county_name
  is '������';
comment on column SD_T_MENDIANXINXI.city_division
  is '������';
comment on column SD_T_MENDIANXINXI.county_division
  is '������';
comment on column SD_T_MENDIANXINXI.business_type
  is 'ҵ������';
comment on column SD_T_MENDIANXINXI.site_states
  is '�ŵ�״̬';
comment on column SD_T_MENDIANXINXI.person_name
  is 'ҵ������';
comment on column SD_T_MENDIANXINXI.person_id
  is 'ҵ��֤����';
comment on column SD_T_MENDIANXINXI.address
  is '��ϵ��ַ';
comment on column SD_T_MENDIANXINXI.phone
  is '��ϵ��ʽ';
comment on column SD_T_MENDIANXINXI.ems_code
  is '��������';
comment on column SD_T_MENDIANXINXI.out_min_money
  is 'ת�����׽��';
comment on column SD_T_MENDIANXINXI.transfer_min_money
  is 'ת�˱��׽��';
comment on column SD_T_MENDIANXINXI.relationship
  is '�ŵ꾺����ϵ';
comment on column SD_T_MENDIANXINXI.site_level
  is '�ŵ꼶�����';
comment on column SD_T_MENDIANXINXI.channel_1
  is '��������1';
comment on column SD_T_MENDIANXINXI.channel_2
  is '��������2';
comment on column SD_T_MENDIANXINXI.channel_3
  is '��������3';
comment on column SD_T_MENDIANXINXI.send_pattern
  is '�ַ�ģʽ';
comment on column SD_T_MENDIANXINXI.manage_sr
  is '����-SR';
comment on column SD_T_MENDIANXINXI.move_sr1
  is 'ת��SR1';
comment on column SD_T_MENDIANXINXI.move_sr2
  is 'ת��SR2';
comment on column SD_T_MENDIANXINXI.move_sr3
  is 'ת��SR3';
comment on column SD_T_MENDIANXINXI.distribution_1
  is '����SR1';
comment on column SD_T_MENDIANXINXI.distribution_2
  is '����SR2';
comment on column SD_T_MENDIANXINXI.distribution_3
  is '����SR3';
comment on column SD_T_MENDIANXINXI.order_warehouse
  is '�����ֿ�';
comment on column SD_T_MENDIANXINXI.refund_ticket_permit
  is '����Ʊ���';
comment on column SD_T_MENDIANXINXI.submit_order_permit
  is '�����ύ���';
comment on column SD_T_MENDIANXINXI.sure_active_mony
  is '����ȷ�����';
comment on column SD_T_MENDIANXINXI.manual_activation_permit
  is '�ֹ��������';
comment on column SD_T_MENDIANXINXI.order_automatic_permit
  is '�����Զ��������';
comment on column SD_T_MENDIANXINXI.sale_commission_proportion
  is '����Ӷ�����';
comment on column SD_T_MENDIANXINXI.sale_commission_modul
  is '����Ӷ��ģʽ';
comment on column SD_T_MENDIANXINXI.sale_commission_way
  is '����Ӷ��������';
comment on column SD_T_MENDIANXINXI.sale_commission_pay
  is '����Ӷ��֧����ʽ';
comment on column SD_T_MENDIANXINXI.duijiang_commission_proportion
  is '�ҽ�Ӷ�����';
comment on column SD_T_MENDIANXINXI.duijiang_commission_modul
  is '�ҽ�Ӷ��ģʽ';
comment on column SD_T_MENDIANXINXI.duijiang_commission_way
  is '�ҽ�Ӷ��������';
comment on column SD_T_MENDIANXINXI.duijiang_commission_pay
  is '�ҽ�Ӷ��֧����ʽ';
comment on column SD_T_MENDIANXINXI.duijiang_max_money
  is '�ҽ�Ӷ������޶�';
comment on column SD_T_MENDIANXINXI.duijiang_min_money
  is '�ҽ�Ӷ������޶�';
comment on column SD_T_MENDIANXINXI.duijiang_pay_sure_money
  is '�ҽ�֧��ȷ�Ͻ��';
comment on column SD_T_MENDIANXINXI.cycle
  is '����';
comment on column SD_T_MENDIANXINXI.duijiang_times
  is '�ҽ�����';
comment on column SD_T_MENDIANXINXI.clock_time
  is '����ʱ��';
comment on column SD_T_MENDIANXINXI.receive_person
  is '�����ջ���';
comment on column SD_T_MENDIANXINXI.receive_address
  is '�����ջ���ַ';
comment on column SD_T_MENDIANXINXI.receive_phone
  is '���͵绰���ջ��˵绰��';
comment on column SD_T_MENDIANXINXI.manage_date
  is '����';
-- Create/Recreate primary, unique and foreign key constraints 
alter table SD_T_MENDIANXINXI
  add constraint SD_T_MENDIANXINXI_PK primary key (ID)
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
