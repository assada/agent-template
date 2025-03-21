from app.infrastructure.redis_consumer import RedisConsumer

def run():
    RedisConsumer().consume()

if __name__ == "__main__":
    run()
