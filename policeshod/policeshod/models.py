from django.db import models


class news_details(models.Model):
    "Table to store news details"
    news_id = models.AutoField(primary_key=True,db_column='news_id')
    news_title = models.TextField(db_column='news_title')
    news_subtitle = models.TextField(db_column='news_subtitle', null=True)
    news_imp_text = models.TextField(db_column='news_imp_text',null=True)
    news_full_text = models.TextField(db_column='news_full_text')
    news_image = models.ImageField(db_column='news_image', upload_to='assets/images/thumbnails/', null=True, default=None)
    news_source = models.TextField(db_column='news_source')
    news_category = models.TextField(db_column='news_category')
    news_subcategory = models.TextField(db_column='news_subcategory')
    news_location = models.TextField(db_column='news_location')
    news_reporter = models.TextField(db_column='news_reporter')
    news_received_date = models.DateField(db_column='news_received_date')
    news_publish_date = models.DateField(db_column='news_publish_date')
    news_created_by = models.TextField(db_column='news_created_by')
    news_updated_by = models.TextField(db_column='news_updated_by')
    news_is_active = models.BooleanField(db_column='news_is_active', default=1)

    def __unicode__(self):
        return self.news_id


class news_editorial(models.Model):
    "Table to store the editorial"
    editorial_id = models.AutoField(primary_key=True, db_column='editorial_id')
    editorial_title = models.TextField(db_column='editorial_title')
    editorial_subtitle = models.TextField(db_column='editorial_subtitle', null=True)
    editorial_imp_text = models.TextField(db_column='editorial_imp_text', null=True)
    editorial_full_text = models.TextField(db_column='editorial_full_text')
    editorial_image = models.ImageField(db_column='editorial_image', upload_to='assets/images/thumbnails/',
                                        null=True, default=None)
    # editorial_source = models.TextField(db_column='editorial_source')
    # editorial_category = models.TextField(db_column='editorial_category')
    # editorial_subcategory = models.TextField(db_column='editorial_subcategory')
    # editorial_location = models.TextField(db_column='editorial_location')
    editorial_writer = models.TextField(db_column='editorial_writer')
    editorial_received_date = models.DateField(db_column='editorial_received_date')
    editorial_publish_date = models.DateField(db_column='editorial_publish_date')
    editorial_created_by = models.TextField(db_column='editorial_created_by')
    editorial_updated_by = models.TextField(db_column='editorial_updated_by')
    editorial_is_active = models.BooleanField(db_column='editorial_is_active', default=1)

    def __unicode__(self):
        return self.editorial_id


class breaking_news(models.Model):
    "table to store breaking news"
    breaking_news_id = models.AutoField(primary_key=True, db_column='breaking_news_id')
    breaking_news_title = models.TextField(db_column='breaking_news_title')
    breaking_news_subtitle = models.TextField(db_column='breaking_news_subtitle', null=True)
    breaking_news_imp_text = models.TextField(db_column='breaking_news_imp_text', null=True)
    breaking_news_full_text = models.TextField(db_column='breaking_news_full_text')
    breaking_news_image = models.ImageField(db_column='breaking_news_image', upload_to='assets/images/thumbnails/',
                                        null=True, default=None)
    breaking_news_source = models.TextField(db_column='breaking_news_source')
    breaking_news_category = models.TextField(db_column='breaking_news_category')
    breaking_news_subcategory = models.TextField(db_column='breaking_news_subcategory')
    breaking_news_location = models.TextField(db_column='breaking_news_location')
    breaking_news_reporter = models.TextField(db_column='breaking_news_reporter')
    breaking_news_received_date = models.DateField(db_column='breaking_news_received_date')
    breaking_news_publish_date = models.DateField(db_column='breaking_news_publish_date')
    breaking_news_created_by = models.TextField(db_column='breaking_news_created_by')
    breaking_news_updated_by = models.TextField(db_column='breaking_news_updated_by')
    breaking_news_is_active = models.BooleanField(db_column='breaking_news_is_active', default=1)

    def __unicode__(self):
        return self.breaking_news_title


class main_news(models.Model):
    "table to store main news"
    main_news_id = models.AutoField(primary_key=True, db_column='main_news_id')
    main_news_title = models.TextField(db_column='main_news_title')
    main_news_subtitle = models.TextField(db_column='main_news_subtitle', null=True)
    main_news_imp_text = models.TextField(db_column='main_news_imp_text', null=True)
    main_news_full_text = models.TextField(db_column='main_news_full_text')
    main_news_image = models.ImageField(db_column='main_news_image', upload_to='assets/images/thumbnails/',
                                            null=True, default=None)
    main_news_source = models.TextField(db_column='main_news_source')
    main_news_category = models.TextField(db_column='main_news_category')
    main_news_subcategory = models.TextField(db_column='main_news_subcategory')
    main_news_location = models.TextField(db_column='main_news_location')
    main_news_reporter = models.TextField(db_column='main_news_reporter')
    main_news_received_date = models.DateField(db_column='main_news_received_date')
    main_news_publish_date = models.DateField(db_column='main_news_publish_date')
    main_news_created_by = models.TextField(db_column='main_news_created_by')
    main_news_updated_by = models.TextField(db_column='main_news_updated_by')
    main_news_is_active = models.BooleanField(db_column='main_news_is_active', default=1)

    def __unicode__(self):
        return self.main_news_id


class khandesh_news(models.Model):
    "table to store main news"
    khandesh_news_id = models.AutoField(primary_key=True, db_column='khandesh_news_id')
    khandesh_news_title = models.TextField(db_column='khandesh_news_title')
    khandesh_news_subtitle = models.TextField(db_column='khandesh_news_subtitle', null=True)
    khandesh_news_imp_text = models.TextField(db_column='khandesh_news_imp_text', null=True)
    khandesh_news_full_text = models.TextField(db_column='khandesh_news_full_text')
    khandesh_news_image = models.ImageField(db_column='khandesh_news_image', upload_to='assets/images/thumbnails/',
                                            null=True, default=None)
    khandesh_news_source = models.TextField(db_column='khandesh_news_source')
    khandesh_news_category = models.TextField(db_column='khandesh_news_category')
    khandesh_news_subcategory = models.TextField(db_column='khandesh_news_subcategory')
    khandesh_news_location = models.TextField(db_column='khandesh_news_location')
    khandesh_news_reporter = models.TextField(db_column='khandesh_news_reporter')
    khandesh_news_received_date = models.DateField(db_column='khandesh_news_received_date')
    khandesh_news_publish_date = models.DateField(db_column='khandesh_news_publish_date')
    khandesh_news_created_by = models.TextField(db_column='khandesh_news_created_by')
    khandesh_news_updated_by = models.TextField(db_column='khandesh_news_updated_by')
    khandesh_news_is_active = models.BooleanField(db_column='khandesh_news_is_active', default=1)

    def __unicode__(self):
        return self.khandesh_news_id


class dhule_special_news(models.Model):
    "Table to store news details"
    dhule_special_news_id = models.AutoField(primary_key=True,db_column='dhule_special_news_id')
    dhule_special_news_title = models.TextField(db_column='dhule_special_news_title')
    dhule_special_news_subtitle = models.TextField(db_column='dhule_special_news_subtitle', null=True)
    dhule_special_news_imp_text = models.TextField(db_column='dhule_special_news_imp_text',null=True)
    dhule_special_news_full_text = models.TextField(db_column='dhule_special_news_full_text')
    dhule_special_news_image = models.ImageField(db_column='dhule_special_news_image', upload_to='assets/images/thumbnails/', null=True, default=None)
    dhule_special_news_source = models.TextField(db_column='dhule_special_news_source')
    dhule_special_news_category = models.TextField(db_column='dhule_special_news_category')
    dhule_special_news_subcategory = models.TextField(db_column='dhule_special_news_subcategory')
    dhule_special_news_location = models.TextField(db_column='dhule_special_news_location')
    dhule_special_news_reporter = models.TextField(db_column='dhule_special_news_reporter')
    dhule_special_news_received_date = models.DateField(db_column='dhule_special_news_received_date')
    dhule_special_news_publish_date = models.DateField(db_column='dhule_special_news_publish_date')
    dhule_special_news_created_by = models.TextField(db_column='dhule_special_news_created_by')
    dhule_special_news_updated_by = models.TextField(db_column='dhule_special_news_updated_by')
    dhule_special_news_is_active = models.BooleanField(db_column='dhule_special_news_is_active', default=1)

    def __unicode__(self):
        return self.dhule_special_news_id


class mix_news(models.Model):
    "table to store mix news"
    mix_news_id = models.AutoField(primary_key=True, db_column='mix_news_id')
    mix_news_title = models.TextField(db_column='mix_news_title')
    mix_news_subtitle = models.TextField(db_column='mix_news_subtitle', null=True)
    mix_news_imp_text = models.TextField(db_column='mix_news_imp_text', null=True)
    mix_news_full_text = models.TextField(db_column='mix_news_full_text')
    mix_news_image = models.ImageField(db_column='mix_news_image', upload_to='assets/images/thumbnails/', null=True,
                                   default=None)
    mix_news_source = models.TextField(db_column='mix_news_source')
    mix_news_category = models.TextField(db_column='mix_news_category')
    mix_news_subcategory = models.TextField(db_column='mix_news_subcategory')
    mix_news_location = models.TextField(db_column='mix_news_location')
    mix_news_reporter = models.TextField(db_column='mix_news_reporter')
    mix_news_received_date = models.DateField(db_column='mix_news_received_date')
    mix_news_publish_date = models.DateField(db_column='mix_news_publish_date')
    mix_news_created_by = models.TextField(db_column='mix_news_created_by')
    mix_news_updated_by = models.TextField(db_column='mix_news_updated_by')
    mix_news_is_active = models.BooleanField(db_column='mix_news_is_active', default=1)

    def __unicode__(self):
        return self.mix_news_id