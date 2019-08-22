from django.db import models

# Create your models here.
class Rumour(models.Model):
    rumour_id = models.AutoField(primary_key = True)
    rumour_content = models.TextField()
    rumour_predicted_label = models.IntegerField()
    rumour_prediced_prob = models.FloatField()
    rumour_true_label = models.IntegerField()
    rumour_submit_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.rumour_content
