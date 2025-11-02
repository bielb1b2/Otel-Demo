package com.example.otel_demo.controllers;

import com.github.benmanes.caffeine.cache.Cache;
import com.github.benmanes.caffeine.cache.Caffeine;
import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.Duration;

@RestController
@RequestMapping("/flow")
public class FlowController {

    private static final Logger logger = LoggerFactory.getLogger(FlowController.class);

    private final MeterRegistry meterRegistry;
    private final Cache<String, Counter> startCounters;
    private final Cache<String, Counter> endCounters;

    public FlowController(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        this.startCounters = Caffeine.newBuilder()
                .expireAfterAccess(Duration.ofHours(1))
                .maximumSize(2000)
                .build();
        this.endCounters = Caffeine.newBuilder()
                .expireAfterAccess(Duration.ofHours(1))
                .maximumSize(2000)
                .build();
    }

    @GetMapping("/start/{clientId}")
    public String startFlow(@PathVariable String clientId) {
        Counter counter = startCounters.get(clientId, id ->
                Counter.builder("flow_start_total")
                        .description("Quantidade de fluxos iniciados por cliente")
                        .tag("client_id", id)
                        .register(meterRegistry)
        );
        counter.increment();

        logger.info("Fluxo iniciado para client_id={} | Total: {}", clientId, counter.count());
        return "Fluxo " + clientId + " iniciado!";
    }

    @GetMapping("/end/{clientId}")
    public String endFlow(@PathVariable String clientId) {
        Counter counter = endCounters.get(clientId, id ->
                Counter.builder("flow_end_total")
                        .description("Quantidade de fluxos finalizados por cliente")
                        .tag("client_id", id)
                        .register(meterRegistry)
        );

        counter.increment();
        logger.info("Fluxo finalizado para client_id={} | Total: {}", clientId, counter.count());
        return "Fluxo " + clientId + " finalizado!";
    }

}
